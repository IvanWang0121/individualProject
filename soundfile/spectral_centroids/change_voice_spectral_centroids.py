from tensorflow.keras.models import load_model
import numpy as np

# 加载模型
generator = load_model(r'D:\individualProject\soundfile\spectral_centroids\generator_model_spectral_centroids.h5')

# 加载特征
spectral_centroids_new = np.load(r'D:\individualProject\soundfile\spectral_centroids\common_voice_en_38365575_spectral.npy')

if spectral_centroids_new.shape != (253,):
    print("特征形状不匹配，需要调整。")
    # 调整形状的代码
# 女性条件标签
female_condition = np.array([[1]])

# 假设spectral_centroids_new已经是正确的形状
converted_female_spectral_centroids = generator.predict([spectral_centroids_new.reshape(1, -1), female_condition])

# 保存转换后的特征
np.save(r'D:\individualProject\soundfile\spectral_centroids\converted_female_spectral_centroids.npy', converted_female_spectral_centroids)