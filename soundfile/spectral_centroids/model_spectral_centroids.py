from tensorflow.keras.layers import Input, Dense, Reshape, Conv1D, BatchNormalization, Activation, Concatenate, \
    LeakyReLU, Flatten, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
import numpy as np


def build_generator(input_dim, condition_dim, time_steps=12, features=326):
    input_noise = Input(shape=(input_dim,))
    condition = Input(shape=(condition_dim,))

    merged = Concatenate()([input_noise, condition])
    x = Dense(128, activation='relu')(merged)
    x = Reshape((time_steps, int(128 / time_steps)))(x)  # Adjust the reshape operation based on the dense layer output

    x = Conv1D(filters=64, kernel_size=3, padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    x = Conv1D(filters=features, kernel_size=3, padding='same')(x)
    x = Activation('tanh')(x)

    generator = Model(inputs=[input_noise, condition], outputs=x)
    return generator


def build_discriminator(time_steps=12, features=326):
    input_shape = (time_steps, features,)
    input_data = Input(shape=input_shape)

    x = Conv1D(filters=64, kernel_size=3, strides=2, padding="same")(input_data)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dropout(0.3)(x)

    x = Flatten()(x)
    validity = Dense(1, activation='sigmoid')(x)

    discriminator = Model(inputs=input_data, outputs=validity)
    return discriminator

# 输入维度为1，因为每个频谱质心特征是一个标量值
input_dim = 100
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

# 加载特征
spectral_centroids_male_path = 'D:\individualProject\soundfile\spectral_centroids\combined_spectral_array_male.npy'
spectral_centroids_male_path = np.load(spectral_centroids_male_path).reshape(-1, 1)
spectral_centroids_female_path = 'D:\individualProject\soundfile\spectral_centroids\combined_spectral_array_female.npy'
spectral_centroids_female_path = np.load(spectral_centroids_female_path).reshape(-1, 1)

male_conditions = np.zeros((spectral_centroids_male_path.shape[0], 1))
female_conditions = np.ones((spectral_centroids_female_path.shape[0], 1))

epochs = 2500
batch_size = 32
half_batch = int(batch_size / 2)

for epoch in range(epochs):
    idx = np.random.randint(0, spectral_centroids_male_path.shape[0], half_batch)
    male_samples = spectral_centroids_male_path[idx]
    female_samples = spectral_centroids_female_path[idx]

    noise = np.random.normal(0, 1, (half_batch, input_dim))
    generated_samples = generator.predict([noise, np.ones((half_batch, 1))])

    d_loss_real = discriminator.train_on_batch([female_samples, np.ones((half_batch, 1))], np.ones((half_batch, 1)))
    d_loss_fake = discriminator.train_on_batch([generated_samples, np.ones((half_batch, 1))], np.zeros((half_batch, 1)))
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    noise = np.random.normal(0, 1, (batch_size, input_dim))
    valid_y = np.array([1] * batch_size)

    g_loss = combined.train_on_batch([noise, np.ones((batch_size, 1))], valid_y)

    print("%d [判别器损失: %f, 准确度: %.2f%%] [生成器损失: %f]" % (epoch, d_loss[0], 100 * d_loss[1], g_loss))

generator.save('generator_model_spectral_centroids.h5')



