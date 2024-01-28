import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import os
from sklearn.model_selection import train_test_split


folder_path = 'D:\\individualProject\\soundfile\\female_features_spectral_centroids'
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.npy')]

features_list = []

for file_path in file_paths:
    # 加载每个文件
    feature = np.load(file_path)
    features_list.append(feature)

# 将列表转换为一个NumPy数组
features_array = np.array(features_list)

print("Combined features shape:", features_array.shape)

np.save('combined_spectral_array_female', features_array)