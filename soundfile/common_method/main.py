import librosa
import numpy as np
import os
import soundfile as sf

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
    y_adjusted = librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps)
    return y_adjusted



male_folder_path = 'D:\individualProject\soundfile\male'
pitch_means = []
for filename in os.listdir(male_folder_path):
    file_path = os.path.join(male_folder_path, filename)
    male_pitch_mean, sr = load_audio_and_calculate_pitch_mean(file_path)
    pitch_means.append(male_pitch_mean)
print(len(pitch_means))
means = np.array(pitch_means)
np.save('meansdata.npy', means)
maletarget_pitch_mean = np.mean(means)


female_voice_path = 'D:\\individualProject\\soundfile\\female\\common_voice_en_38024629.mp3'
#改为变量，接受数据

y_female_adjusted = adjust_audio_pitch(female_voice_path, sr, maletarget_pitch_mean)

output_path = 'adjusted_female_voice.wav'
#改为桌面的位置（用户选择）
sf.write(output_path, y_female_adjusted, sr)