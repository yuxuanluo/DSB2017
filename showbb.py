import os
import numpy as np
import matplotlib.pyplot as plt

# path = 'prep_result/'

# for file in os.listdir(path):
#     if file.endswith('clean.npy'):
#         print(file)
#         img = np.load(path + file)
#         img = img / 255.0
#         # img /= 255.0
#         # print(img.shape)
#         # print(img.max())
#         # print(img.min())
#         for i in range(10):
#             plt.imshow(img[0, 20 + 20 * i], cmap="Greys")
#             plt.show()
#         print()
#         # break

# for file in os.listdir(path):
#     if file.endswith('label.npy'):
#         print(file)
#         img = np.load(path + file)
#         # img /= 255.0
#         print(img.shape)
#         print(img)
#         # print(img.max())
#         # print(img.min())
#         print()
#         # break


path = 'bbox_result/'
for file in os.listdir(path):
    if file.endswith('pbb.npy'):
        print(file)
        img = np.load(path + file)
        print(img.shape)
        print(img)
        # img = img / 255.0
        # print(img.max())
        # print(img.min())

        # for i in range(10):
        #     plt.imshow(img[0, 20 + 20 * i], cmap="Greys")
        #     plt.show()
        print()
        break
