import os
import numpy as np
from collections import Counter

folder_path = r'D:\individualProject\soundfile\female_features_chroma'
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.npy')]


shapes = [np.load(file).shape for file in file_paths]


shape_counter = Counter(shapes)
most_common_shape = shape_counter.most_common(1)[0][0]
print(most_common_shape)


consistent_feature_files = [file for file, shape in zip(file_paths, shapes) if shape == most_common_shape]

features_list = [np.load(file) for file in consistent_feature_files]

features_array = np.array(features_list)
print("Combined consistent features shape:", features_array.shape)

np.save('combined_chroma_array_female.npy', features_array)
