import matplotlib.pyplot as plt
import numpy as np
import cv2

a = cv2.imread(r"D:\macro_2023\crop\1027.png")
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# cv2.imshow('asfd', a)
# cv2.waitKey()
# cv2.destroyWindow('asdf')
a[a < 200] = 0
a[a < 215] = 0
# a[a >= 200] = 255
y, x = np.where(a > 200)
print(x)
for i in x:
    print(type(i))

plt.imshow(a, cmap='gray')

# for i in range(len(x)):
#     print(x[i], y[i])
#     plt.scatter(x[i], y[i], s=7, marker='.', c='b')
#     if i == 1000:
#         break

# plt.axis('off')
# plt.savefig('D:\macro_2023\scatter/myplot.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()


