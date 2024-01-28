import librosa
import numpy as np
import os

male_audio_folder = 'D:\\individualProject\\soundfile\\female'
output_folder = 'D:\\individualProject\\soundfile\\female_features_spectral_centroids'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def extract_features(file_path):
    y, sr = librosa.load(file_path)
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

    # calculate mean
    return np.mean(spectral_centroids)


for file_name in os.listdir(male_audio_folder):
    if file_name.endswith('.mp3'):
        file_path = os.path.join(male_audio_folder, file_name)

        features = extract_features(file_path)

        npy_file_name = os.path.splitext(file_name)[0] + '_features.npy'
        npy_file_path = os.path.join(output_folder, npy_file_name)
        np.save(npy_file_path, features)