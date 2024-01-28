import librosa
import numpy as np

data = np.load('D:\individualProject\soundfile\common_voice_en_38365575.npy',allow_pickle= True)

mfccs_mean = np.mean(data, axis=1)

print(mfccs_mean.shape)

np.save('average_common_voice_en_38365575',data)
#no cut -will lose data reduce accuacy