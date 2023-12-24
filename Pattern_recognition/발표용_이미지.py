import matplotlib.pyplot as plt
import numpy as np
import cv2

a = cv2.imread(r"D:\macro_2023\crop\17.png")
#
# a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# print(a.shape)
plt.imshow(a, cmap='gray')
plt.show()

a = np.array([[1, 1, 0], [2, 1, 1], [0, 1, 0]])

print(np.linalg.det(a))

# plt.imshow(a, cmap='gray')
# plt.axis('off')
# plt.savefig('D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지/gray.png', pad_inches=0, bbox_inches='tight')