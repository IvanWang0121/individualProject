import pandas as pd

file_path = 'D:\individualProject\soundfile\other.tsv'
data = pd.read_csv(file_path, sep='\t')

male_data = data[data['gender'] == 'male'].head(1000)
female_data = data[data['gender'] == 'female'].head(1000)

male_data.to_csv('male_data.tsv', sep='\t', index=False)
female_data.to_csv('female_data.tsv', sep='\t', index=False)