from tensorflow.keras.layers import Input, Dense, Dropout, LeakyReLU, BatchNormalization, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np

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


input_dim = 13
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



male_mfccs = np.load('D:\\individualProject\\soundfile\\mfcc\\features_array_male.npy')
female_mfccs = np.load('D:\\individualProject\\soundfile\\mfcc\\features_array_female.npy')

male_conditions = np.zeros((male_mfccs.shape[0], 1))
female_conditions = np.ones((female_mfccs.shape[0], 1))

epochs = 2500
batch_size = 32
half_batch = int(batch_size / 2)

for epoch in range(epochs):
    # 随机选择一半的男性和女性MFCCs
    idx = np.random.randint(0, male_mfccs.shape[0], half_batch)
    male_samples = male_mfccs[idx]
    female_samples = female_mfccs[idx]

    # 生成一半的假女性MFCCs
    noise = np.random.normal(0, 1, (half_batch, input_dim))
    generated_samples = generator.predict([noise, np.ones((half_batch, 1))])

    d_loss_real = discriminator.train_on_batch([female_samples, np.ones((half_batch, 1))], np.ones((half_batch, 1)))
    d_loss_fake = discriminator.train_on_batch([generated_samples, np.ones((half_batch, 1))], np.zeros((half_batch, 1)))
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    noise = np.random.normal(0, 1, (batch_size, input_dim))
    valid_y = np.array([1] * batch_size)

    g_loss = combined.train_on_batch([noise, np.ones((batch_size, 1))], valid_y)

    print("%d [判别器损失: %f, 准确度: %.2f%%] [生成器损失: %f]" % (epoch, d_loss[0], 100 * d_loss[1], g_loss))

generator.save('generator_model_mfcc.h5')



# mfccs_new = np.load('D:\\individualProject\\soundfile\\common_voice_en_3836555.npy')
# mfccs_new = np.expand_dims(mfccs_new, axis=0)
#
# female_condition = np.array([[1]])
#
# mfccs_new_reshaped = np.reshape(mfccs_new, (mfccs_new.shape[0], -1))
# converted_female_mfcc = generator.predict([mfccs_new_reshaped, female_condition])
#
# np.save('converted_female_mfcc.npy', converted_female_mfcc)