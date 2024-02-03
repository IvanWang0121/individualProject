from tensorflow.keras.layers import Input, Dense, Dropout, LeakyReLU, BatchNormalization, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
from tensorflow.keras.layers import Reshape

def build_generator(input_dim, condition_dim):
    input_noise = Input(shape=(input_dim,))
    condition = Input(shape=(condition_dim,))

    merged = Concatenate()([input_noise, condition])

    x = Dense(128)(merged)
    x = LeakyReLU(alpha=0.01)(x)
    x = BatchNormalization(momentum=0.8)(x)

    x = Dense(256)(x)
    x = LeakyReLU(alpha=0.01)(x)
    x = BatchNormalization(momentum=0.8)(x)

    x = Dense(input_dim, activation='tanh')(x)

    generator = Model(inputs=[input_noise, condition], outputs=x)

    return generator


def build_discriminator(input_dim, condition_dim):
    input_data = Input(shape=(input_dim,))
    condition = Input(shape=(condition_dim,))

    merged = Concatenate()([input_data, condition])

    x = Dense(128)(merged)
    x = LeakyReLU(alpha=0.01)(x)
    x = Dropout(0.3)(x)

    x = Dense(256)(x)
    x = LeakyReLU(alpha=0.01)(x)
    x = Dropout(0.3)(x)

    validity = Dense(1, activation='sigmoid')(x)

    discriminator = Model(inputs=[input_data, condition], outputs=validity)

    return discriminator

# 输入维度为1，因为每个频谱质心特征是一个标量值
input_dim = 1
condition_dim = 1

generator = build_generator(input_dim, condition_dim)
discriminator = build_discriminator(input_dim, condition_dim)

discriminator.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5), metrics=['accuracy'])

z = Input(shape=(input_dim,))
condition = Input(shape=(condition_dim,))
generated_sample = generator([z, condition])

discriminator.trainable = False

validity = discriminator([generated_sample, condition])

combined = Model([z, condition], validity)
combined.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))


chroma_male_path = 'D:\individualProject\soundfile\Chroma\combined_chroma_array_male.npy'
chroma_male_path = np.load(chroma_male_path).reshape(-1, 1)
chroma_female_path = 'D:\\individualProject\\soundfile\\Chroma\\newcombined_chroma_array_female.npy'
chroma_female_path = np.load(chroma_female_path).reshape(-1, 1)

male_conditions = np.zeros((chroma_male_path.shape[0], 1))
female_conditions = np.ones((chroma_female_path.shape[0], 1))

epochs = 2500
batch_size = 32
half_batch = int(batch_size / 2)

for epoch in range(epochs):
    idx = np.random.randint(0, chroma_male_path.shape[0], half_batch)
    male_samples = chroma_male_path[idx]
    female_samples = chroma_female_path[idx]

    noise = np.random.normal(0, 1, (half_batch, input_dim))
    generated_samples = generator.predict([noise, np.ones((half_batch, 1))])

    d_loss_real = discriminator.train_on_batch([female_samples, np.ones((half_batch, 1))], np.ones((half_batch, 1)))
    d_loss_fake = discriminator.train_on_batch([generated_samples, np.ones((half_batch, 1))], np.zeros((half_batch, 1)))
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    noise = np.random.normal(0, 1, (batch_size, input_dim))
    valid_y = np.array([1] * batch_size)

    g_loss = combined.train_on_batch([noise, np.ones((batch_size, 1))], valid_y)

    print("%d [判别器损失: %f, 准确度: %.2f%%] [生成器损失: %f]" % (epoch, d_loss[0], 100 * d_loss[1], g_loss))

generator.save('generator_model_chroma.h5')