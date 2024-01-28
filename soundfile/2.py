import pandas as pd
import shutil
import os

male_tsv = 'D:/individualProject/soundfile/female_data.tsv'
clips_folder = 'D:/individualProject/soundfile/clips'
output_folder = 'D:/individualProject/soundfile/female'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

male_data = pd.read_csv(male_tsv, sep='\t')
for file_name in male_data['path']:
    source_file = os.path.join(clips_folder, file_name)
    target_file = os.path.join(output_folder, file_name)
    if os.path.exists(source_file):
        shutil.copy(source_file, target_file)