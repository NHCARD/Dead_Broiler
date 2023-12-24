import glob
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
# from scipy.spatial import distance
import func

# a = glob.glob(r'D:\macro_2023\crop/*.png')
b = glob.glob('D:\macro_2023\crop_pred/*.png')


def d_broiler_find(crop_dir, xywh):
    num = 0
    print(xywh)
    a = glob.glob(crop_dir)

    init_img = cv2.imread(a[0])
    img_h = init_img.shape[0]
    img_w = init_img.shape[1]

    aaa = np.zeros((img_h, img_w))


    for i, j in zip(a, b):
        print(i)
        # if i == r'D:\macro_2023\crop\26.png':
        #     break
        # print(i)
        crop_img = cv2.imread(i)
        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('asdf', crop_img)
        # cv2.waitKey(0)

        # pred_img = cv2.imread(j)
        # pred_img = cv2.cvtColor(pred_img, cv2.COLOR_BGR2GRAY)
        # res, masked_thr = cv2.threshold(pred_img, 110, 255, cv2.THRESH_BINARY)

        # mask_true = np.where(masked_thr == 255)
        # for k in range(len(mask_true[0])):
        #     crop_img[mask_true[0][k]][mask_true[1][k]] = 0

        crop_img[crop_img < 210] = 0
        crop_img[crop_img > 245] = 0
        crop_img[245 >= np.all(crop_img) >= 210] = 0

        non_zero = np.where(crop_img != 0)
        print(len(non_zero[0]))

        # plt.imshow(crop_img, cmap='gray')
        # plt.axis('off')
        # plt.savefig(fr"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지\{num+1:0>2d}.png", pad_inches=0, bbox_inches='tight')
        # plt.show()

        over_hundred = []
        for x, y in zip(non_zero[1], non_zero[0]):
            crop_x, crop_y, w, h = func.get_crop(x, y, crop_img, img_w, img_h)
            # print(type(x), type(y))
            # print(x, y)
            sys.exit()

            count = 0
            for height in range(crop_y, crop_y + h):
                for width in range(crop_x, crop_x + w):
                    if height == 413:
                        print(crop_y, crop_x, h, w)
                        print(y, x, height, width)
                    if crop_img[height, width] == 0:
                        continue
                    if height == y and width == x:
                        continue
                    dist = distance.euclidean([x, y], [width, height])

                    if dist < 4:
                        count += 1

            if count > 25:
                over_hundred.append([x, y])

        zero = np.zeros((img_h, img_w))

        for pos in over_hundred:
            zero[pos[1]][pos[0]] = 255

        # plt.imshow(zero, cmap='gray')
        # plt.show()

        aaa += zero

        # plt.imshow(zero, cmap='gray')
        # plt.axis('off')
        # plt.savefig(fr"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지/zero_map/{num + 1:0>2d}.png", pad_inches=0, bbox_inches='tight')
        # plt.show()

        num += 1

        plt.imshow(zero, cmap='gray')
        plt.savefig(fr'D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지\zero_2/{num:0>2d}.png')
        plt.show()
        # cv2.imshow('asdf', crop_img)
        # cv2.waitKey(0)
        # try:
        #     os.mkdir(fr"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지\non_noise_8x8/{i[-6:]}")
        # except:
        #     pass

        # for x, y in zip(non_zero[1], non_zero[0]):
        #     crop_x, crop_y, w, h = func.get_crop(x, y, zero)
        #     az = zero[crop_y:h, crop_x:crop_x+w]
        #     plt.imshow(az, cmap='gray')
        #     plt.title(f'{x}_{y}_{w}_{h}')
        #     plt.savefig(fr"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지\non_noise_8x8/{i[-6:]}/{x}_{y}_{w}_{h}.png", pad_inches=0, bbox_inches='tight')
        #     plt.show()
    # aaa = aaa / np.max(aaa)
    return aaa

    # print(np.where(aaa == np.max(aaa)))
    pos = np.where(aaa == np.max(aaa))
    img = cv2.imread(r'D:\macro_2023\crop\14.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.imshow(img, cmap='gray')
    plt.scatter(pos[1][0], pos[0][0], s=20, marker='.', c='b')
    plt.title('original')
    plt.axis('off')
    # plt.savefig(r"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지/original.png", pad_inches=0, bbox_inches='tight')
    plt.show()

    aaa = aaa / np.max(aaa)
    plt.imshow(aaa, cmap='gray')
    plt.title('energy matrix')
    plt.axis('off')
    # plt.savefig(r"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지/normalize_energy-matrix.png", pad_inches=0, bbox_inches='tight')
    plt.show()

    matrix_crop = aaa[277 - 60:, 235 - 60:235 + 60]
    matrix_pos = np.where(matrix_crop == np.max(matrix_crop))
    plt.imshow(matrix_crop, cmap='gray')
    plt.title('enrgy matrix crop')
    plt.scatter(matrix_pos[1][0], matrix_pos[0][0], s=40, c='r', marker='.')
    plt.axis('off')
    # plt.savefig(r"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지/energy-matrix_crop.png", pad_inches=0, bbox_inches='tight')
    plt.show()

    plt.imshow(img, cmap='gray')
    plt.scatter(matrix_pos[1][0] + 235 - 60, matrix_pos[0][0] + 277 - 60, s=40, c='r', marker='.')
    plt.title('dead broiler visualize')
    plt.axis('off')
    # plt.savefig(r"D:\macro_2023\Pattern_recognition\마지막_프로세스_발표이미지/dead_broiler_visualize.png", pad_inches=0, bbox_inches='tight')
    plt.show()

# d_broiler_find()