import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r'D:\macro_2023\crop\14.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.show()
plt.imshow(img, cmap='gray')
plt.scatter(122, 273, s=20, marker='.', c='b')
plt.show()
