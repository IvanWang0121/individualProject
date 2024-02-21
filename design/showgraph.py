import matplotlib.pyplot as plt
import numpy as np
import librosa

y1, sr = librosa.load('D:\individualProject\design\hello.wav', sr=44100)
y2, sr = librosa.load("D:/individualProject/design/shifting/new.wav", sr=44100)

# plt.figure(figsize=(12, 8))
#
# plt.subplot(2, 1, 1)
# plt.plot(y1)
# plt.title('First Audio Waveform')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
#
# plt.subplot(2, 1, 2)
# plt.plot(y2)
# plt.title('Second Audio Waveform')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
#
# plt.tight_layout()
# plt.show()

def plot_frequency_spectrum(y, sr, title):
    # FFT
    fft = np.fft.fft(y)
    magnitude = np.abs(fft)
    frequency = np.linspace(0, sr, len(magnitude))

    # draw half
    left_spectrum = magnitude[:int(len(magnitude)/2)]
    left_frequency = frequency[:int(len(frequency)/2)]

    #  draw
    plt.plot(left_frequency, left_spectrum)
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.show()


plot_frequency_spectrum(y1, 44410, "First Audio Waveform")