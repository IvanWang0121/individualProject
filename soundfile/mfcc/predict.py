from tensorflow.keras.models import load_model
import numpy as np

generator = load_model('D:\individualProject\soundfile\mfcc\generator_model_mfcc.h5')

mfccs_new = np.load('D:\individualProject\soundfile\common_voice_en_38365575.npy')

female_condition = np.array([[1]])  # 女性标签

mfccs_new_reshaped = np.mean(mfccs_new, axis=1).reshape(1, -1)
converted_female_mfcc = generator.predict([mfccs_new_reshaped, female_condition])

np.save('converted_female_mfcc.npy', converted_female_mfcc)


# data = np.load('D:\individualProject\soundfile\converted_female_mfcc.npy',allow_pickle= True)

# print(data.shape)