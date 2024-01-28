import librosa
import numpy as np

audio_path = 'D:\individualProject\soundfile\common_voice_en_38365575.mp3'

audio, sr = librosa.load(audio_path, sr=None)

mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

save_path = 'D:\individualProject\soundfile\common_voice_en_38365575.npy'

np.save(save_path, mfccs)