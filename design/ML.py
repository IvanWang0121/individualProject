import numpy as np
import librosa
import matplotlib.pyplot as plt


# select file
y, sr = librosa.load('D:\individualProject\design\hello.wav', sr=44100)

#take feature
mfccs = librosa.feature.mfcc(y=y, sr=44100, n_mfcc=13)
g = librosa.feature.spectral_centroid(y=y, sr=44100)


plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.hist(mfccs.flatten(), bins=10)
plt.title('MFCCs Histogram')
plt.xlabel('MFCC Coefficients')
plt.ylabel('Frequency')

# draw
plt.subplot(2, 1, 2)
plt.hist(g.flatten(), bins=10)
plt.title('Spectral Centroids Histogram')
plt.xlabel('Spectral Centroid')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()