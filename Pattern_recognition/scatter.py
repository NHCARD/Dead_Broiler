import matplotlib.pyplot as plt
import cv2
import os
import glob


def crops(before_xywh, img, idx, dir):
    source = cv2.imread(img)
    crop_img = source[int(before_xywh[0][1] - (before_xywh[0][3] + (before_xywh[0][3] * 0.5))):int(before_xywh[0][1] + (before_xywh[0][3] + (before_xywh[0][3] * 0.5))),
                int(before_xywh[0][0] - (before_xywh[0][2] + (before_xywh[0][2] * 0.5))):int(before_xywh[0][0] + (before_xywh[0][2] + before_xywh[0][2] * 0.5))]
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)

    plt.imshow(crop_img)
    plt.axis('off')
    plt.savefig(f'D:\macro_2023/{dir}/' + f'{idx:0>2d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()
