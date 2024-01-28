import librosa
import numpy as np
import soundfile as sf

def mfcc_to_spectrogram(mfcc, n_mfcc=13, n_fft=2048, hop_length=512):
    mel_spectrogram = librosa.feature.inverse.mfcc_to_mel(mfcc, n_mels=n_mfcc)

    spectrogram = librosa.feature.inverse.mel_to_stft(mel_spectrogram, n_fft=n_fft)
    return spectrogram


def spectrogram_to_audio(spectrogram, sr=22050, n_fft=2048, hop_length=512, n_iter=32):
    audio = librosa.griffinlim(spectrogram, n_iter=n_iter, hop_length=hop_length, win_length=n_fft)
    return audio


mfccs = np.load('D:\individualProject\soundfile\converted_female_mfcc.npy')

n_mfcc = 13
if mfccs.shape[0] == n_mfcc:
    mfccs = mfccs.T

spectrogram = mfcc_to_spectrogram(mfccs)

reconstructed_audio = spectrogram_to_audio(spectrogram)

sf.write('reconstructed_audio.wav', reconstructed_audio, 22050)