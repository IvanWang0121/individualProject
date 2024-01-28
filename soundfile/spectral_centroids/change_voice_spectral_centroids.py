from tensorflow.keras.models import load_model
import numpy as np

generator = load_model('D:\individualProject\soundfile\spectral_centroids\generator_model_spectral_centroids.h5')

spectral_centroids_new = np.load('D:\individualProject\soundfile\spectral_centroids\common_voice_en_38365575_spectral.npy')

female_condition = np.array([[1]])  # 女性标签

spectral_centroids_new_reshaped = np.mean(spectral_centroids_new, axis=1).reshape(1, -1)
converted_female_spectral_centroids = generator.predict([spectral_centroids_new_reshaped, female_condition])

np.save('converted_female_spectral_centroids.npy', converted_female_spectral_centroids)