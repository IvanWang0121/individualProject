import librosa
import numpy as np
import os
import soundfile as sf

from design import globals

def load_audio_and_calculate_pitch_mean(audio_path):

    y, sr = librosa.load(audio_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitches = pitches[magnitudes > np.median(magnitudes)]
    pitch_mean = np.mean(pitches[pitches > 0])
    return pitch_mean, sr


def adjust_audio_pitch(audio_path, sr, target_pitch_mean):

    y, _ = librosa.load(audio_path, sr=sr)
    current_pitch_mean, _ = load_audio_and_calculate_pitch_mean(audio_path)


    # n_steps = globals.n_steps_value_common * np.log2(target_pitch_mean / current_pitch_mean)
    n_steps = 12 * np.log2(target_pitch_mean / current_pitch_mean)

    y_adjusted = librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps)
    return y_adjusted



female_folder_path = 'D:\\individualProject\\soundfile\\female'
pitch_means = []
for filename in os.listdir(female_folder_path):
    file_path = os.path.join(female_folder_path, filename)
    female_pitch_mean, sr = load_audio_and_calculate_pitch_mean(file_path)
    pitch_means.append(female_pitch_mean)
print(len(pitch_means))
means = np.array(pitch_means)
np.save('means_famale_data.npy', means)
femaletarget_pitch_mean = np.mean(means)


male_voice_path = 'D:\individualProject\soundfile\male\common_voice_en_38024742.mp3'
# female_voice_path = globals.selected_files
#改为变量，接受数据

y_male_adjusted = adjust_audio_pitch(male_voice_path, sr, femaletarget_pitch_mean)

output_path = 'adjusted_male_voice.wav'
#改为桌面的位置（用户选择）
sf.write(output_path, y_male_adjusted, sr)