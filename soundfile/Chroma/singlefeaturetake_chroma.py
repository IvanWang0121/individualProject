import librosa
import numpy as np
import os

audio, sr = librosa.load('D:\individualProject\soundfile\common_voice_en_38365575.mp3', sr=44100)

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)[0]

    return chroma

features = extract_features('D:\individualProject\soundfile\common_voice_en_38365575.mp3')
np.save('common_voice_en_38365575_chroma.npy',features)