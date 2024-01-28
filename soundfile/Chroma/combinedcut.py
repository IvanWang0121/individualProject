import os
import numpy as np

features1 = np.load('D:\individualProject\soundfile\Chroma_feature\combined_chroma_array_female.npy')
features2 = np.load('D:\individualProject\soundfile\Chroma_feature\combined_chroma_array_male.npy')
features1_truncated = features1[:, :, :326]

np.save('newcombined_chroma_array_female.npy',features1_truncated)