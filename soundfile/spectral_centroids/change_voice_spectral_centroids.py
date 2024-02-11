import numpy as np
from tensorflow.keras.models import load_model

# 加载模型
generator = load_model(r'D:\individualProject\soundfile\spectral_centroids\generator_model_spectral_centroids.h5')

spectral_centroids_new = np.load(r'D:\individualProject\soundfile\spectral_centroids\common_voice_en_38365575_spectral.npy')

spectral_centroids_new = np.array([[0]])  # 将其重塑为(1, 1)
spectral_centroids_new = np.expand_dims(spectral_centroids_new, axis=-1)
female_condition = np.array([[1]])
female_condition = np.expand_dims(female_condition, axis=-1)

converted_female_spectral_centroids = generator.predict([spectral_centroids_new, female_condition])

np.save(r'D:\individualProject\soundfile\spectral_centroids\coverted_female_spectral_centroids.npy', converted_female_spectral_centroids)