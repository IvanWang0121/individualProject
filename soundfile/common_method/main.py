import librosa
import numpy as np


def load_audio_and_calculate_pitch_mean(audio_path):

    y, sr = librosa.load(audio_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitches = pitches[magnitudes > np.median(magnitudes)]
    pitch_mean = np.mean(pitches[pitches > 0])
    return pitch_mean, sr


def adjust_audio_pitch(audio_path, sr, target_pitch_mean):

    y, _ = librosa.load(audio_path, sr=sr)
    current_pitch_mean, _ = load_audio_and_calculate_pitch_mean(audio_path)


    n_steps = 12 * np.log2(target_pitch_mean / current_pitch_mean)
    y_adjusted = librosa.effects.pitch_shift(y, sr, n_steps)
    return y_adjusted



male_voice_path = 'male_voice.mp3'
male_pitch_mean, sr = load_audio_and_calculate_pitch_mean(male_voice_path)


female_voice_path = 'female_voice.mp3'
y_female_adjusted = adjust_audio_pitch(female_voice_path, sr, male_pitch_mean)


output_path = 'adjusted_female_voice.wav'
librosa.output.write_wav(output_path, y_female_adjusted, sr)