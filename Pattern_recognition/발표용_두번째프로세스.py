import os
import sys

import numpy as np
import cv2
from detect_Fullimg_두번째 import main, parse_opt
import datetime
import glob
import time
import matplotlib.pyplot as plt
import math
from scatter import crops
from test2 import d_broiler_find


def pred():
    stime = datetime.datetime.now()
    img_l = glob.glob(r'D:\macro_2023\Pattern_recognition\vid_cut-Img\0_8_IPC3_20230106080734/*.png')
    before_xywh = None
    print(img_l)
    a = 0
    crop_xywh = None
    for img in img_l:
        opt = parse_opt()
        opt.nosave = True
        opt.exist_ok = True
        opt.test = True
        opt.source = img
        # opt.source = r"C:\Users\inuri64\Downloads\실시간영상_샘플_AdobeExpress.mp4"
        # opt.view_img = True
        # print(datetime.datetime.now())
        xywh = main(opt)

        if before_xywh != None:
            print(img)
            dist = np.sqrt(np.sum((np.array(before_xywh[0][:2]) - np.array(xywh[0][:2])) ** 2))
            print(xywh)

            if dist <= 50 and crop_xywh == None:
                print('chicken!')
                print(dist)

                # plt.imshow(img)
                # plt.show()
                # source = cv2.imread(img)
                # crop_img = source[int(before_xywh[0][1] - (before_xywh[0][3] + (before_xywh[0][3] * 0.5))):int(before_xywh[0][1] + (before_xywh[0][3] + (before_xywh[0][3] * 0.5))),
                #            int(before_xywh[0][0] - (before_xywh[0][2] + (before_xywh[0][2] * 0.5))):int(before_xywh[0][0] + (before_xywh[0][2] + before_xywh[0][2] * 0.5))]
                # print(crop_img.shape)
                # crops(before_xywh, 'D:\macro_2023\predict_img' + img)

                # crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
                # print(crop_img.shape)
                # plt.imshow(crop_img)
                # plt.axis('off')
                # plt.savefig('./crop.png', bbox_inches='tight', pad_inches=0, dpi=300)
                # plt.show()
                crop_xywh = before_xywh
                # for idx, imgg in enumerate(img_l):
                #     crops(crop_xywh, imgg, idx, dir='crop_other')
                # img_ll = os.listdir(r'D:\macro_2023\predict_img')
                # for idx, img in enumerate(img_ll):
                #     crops(before_xywh, 'D:\macro_2023\predict_img/' + img, idx, dir='crop_pred')
                # sys.exit()

            before_img = img

            a += 1
            print(dist)

        if xywh != None:
            before_xywh = xywh
            # visualize(img, xywh)
            # time.sleep(2)

            time.sleep(1)
            print('\n\n')

        if crop_xywh != None and dist > 50:
            stop = img
            asdf = np.ones((300, 300))
            # plt.imshow(asdf)
            # plt.show()
            for idx, imgg in enumerate(img_l):
                if imgg == stop:
                    break
                crops(crop_xywh, imgg, idx, dir='crop')
                # print(crop_xywh)
            energy_matrix = d_broiler_find('D:\macro_2023\crop/*.png', crop_xywh)
            # energy_matrix = np.ones((357, 496))
            # print(energy_matrix.shape)

            max_value = np.max(energy_matrix)
            mat_pos = np.where(energy_matrix == max_value)
            print('asdfasdf')
            plt.imshow(energy_matrix, cmap='gray')
            plt.scatter(mat_pos[1][0], mat_pos[0][0])
            plt.savefig(r'D:\macro_2023\Pattern_recognition/e_matrix2.png', bbox_inches='tight', pad_inches=0)
            plt.show()

            g = cv2.imread(r"D:\macro_2023\crop\14.png")
            g = cv2.cvtColor(g, cv2.COLOR_BGR2RGB)
            # mat_c = energy_matrix[184 - 90:184 + 90, 255 - 90:255+90]
            mat_c = energy_matrix[277 - 60:, 235 - 60:235 + 60]
            # cv2.imshow('asdf', mat_c)
            # cv2.waitKey()
            pos = np.where(np.max(mat_c) == mat_c)
            plt.imshow(g, cmap='gray')
            plt.scatter(pos[1][0] + 235 - 60, pos[0][0] + 217, s=40, c='r', marker='.')
            plt.savefig(r'D:\macro_2023\Pattern_recognition/detect_visualize2.png', bbox_inches='tight', pad_inches=0)
            plt.show()


            break


if __name__ == "__main__":
    sys.path.append('D:\Dead_Broiler\Pattern_recognition\\utils')
    print(sys.path)
    pred()
