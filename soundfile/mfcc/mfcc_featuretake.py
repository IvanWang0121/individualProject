import librosa
import numpy as np
import os


audio, sr = librosa.load('D:\individualProject\soundfile\common_voice_en_38365575.mp3', sr=44100)
# male_audio_folder = 'D:\individualProject\soundfile\common_voice_en_38365575.mp3'
# output_folder = 'D:/individualProject/soundfile/common_voice_en_38365575.npy'

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1)

features = extract_features(audio)
# np.save('common_voice_en_38365575.npy', features)


# for file_name in os.listdir(male_audio_folder):
#     if file_name.endswith('.mp3'):
#         file_path = os.path.join(male_audio_folder, file_name)
#
#         features = extract_features(file_path)
#
#         npy_file_name = os.path.splitext(file_name)[0] + '_features.npy'
#         npy_file_path = os.path.join(output_folder, npy_file_name)
#         np.save(npy_file_path, features)
