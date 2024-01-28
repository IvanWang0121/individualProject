import librosa
import soundfile as sf

# select file
y, sr = librosa.load('D:\individualProject\design\hello.wav', sr=44100)

# exchange pitch

y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=10)

# save file
sf.write('D:\individualProject\design/shifting/new2.wav', y_shifted, sr)


