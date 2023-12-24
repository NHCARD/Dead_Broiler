import glob
import os

import torch
from torch.utils.data import DataLoader

from torchvision import transforms
from PIL import Image
from torch import nn
import cv2
import matplotlib.pyplot as plt

class Unet(nn.Module):
    def __init__(self, img_ch=3, output_ch=1):
        super(Unet, self).__init__()

        self.Maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.Uppool = nn.Upsample(scale_factor=2)
        self.act = nn.LeakyReLU(inplace=True)

        self.e1 = nn.Conv2d(img_ch, 64, kernel_size=3, stride=1, padding=1, bias=True)
        self.e2 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1, bias=True)
        self.e3 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1, bias=True)
        self.e4 = nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1, bias=True)

        self.de1 = nn.Conv2d(512, 256, kernel_size=3, stride=1, padding=1, bias=True)
        self.de2 = nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1, bias=True)
        self.de3 = nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1, bias=True)
        self.de4 = nn.Conv2d(64, output_ch, kernel_size=1, stride=1, padding=0)

    def forward(self, x):
        # encoding path
        x1 = self.act(self.e1(x))
        x2 = self.Maxpool(x1)
        x2 = self.act(self.e2(x2))
        x3 = self.Maxpool(x2)
        x3 = self.act(self.e3(x3))
        x4 = self.Maxpool(x3)
        x4 = self.act(self.e4(x4))
        d4 = self.Uppool(x4)
        # decoding path
        d4 = self.act(self.de1(d4))
        d3 = self.Uppool(d4)
        d3 = self.act(self.de2(d3))
        d2 = self.Uppool(d3)
        d2 = self.act(self.de3(d2))
        out = self.de4(d2)

        return out

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.imageinfo = glob.glob(r"D:\macro_2023\Pattern_recognition\vid_cut-Img\0_8_IPC3_20230106080734/*.png")
        print(self.imageinfo)
        # self.imageinfo = r'D:\\macro_2023\\crop\\1027.png'

        self.data_transforms = transforms.Compose([transforms.ToTensor(),
                                                   ])

    def __len__(self):
        return len(self.imageinfo)

    def __getitem__(self, idx):
        print(self.imageinfo[idx])
        x = cv2.imread(self.imageinfo[idx])
        print(x)
        x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        # x = cv2.resize(x, (512, 512))

        x = self.data_transforms(x)
        # print(x.shape)

        return x



device = "cuda:0"
model = torch.load('./segnet.pth')

dataset = CustomDataset()
# data = dataset.__getitem__(0)
# print(data)
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
# img = cv2.imread(r"D:\yolov5\person\train\images\20221105_ch2_1429.png")
# img = cv2.resize(img, (224, 224))
# img =
# print(type(img))

if __name__ == '__main__':
    for batch_idx, samples in enumerate(dataloader):
        inputs = samples

        inputs = inputs.to(device)
        print(inputs.shape)

        outputs = model(inputs)
        outputs = outputs.cpu().detach().numpy()
        print(outputs.shape)
        # cv2.imwrite(f'./dd/{batch_idx}.png', outputs[0][0])
        # plt.figure(figsize=(8, 6))
        plt.imshow(outputs[0][0], cmap='gray')
        plt.show()
        plt.imsave(f'D:\macro_2023\predict_img/{batch_idx:0>2d}.png', outputs[0][0], cmap='gray')

    # for i in range(0, 256, 5):
    #     res, masked_thr = cv2.threshold(outputs[0][0], i, 255, cv2.THRESH_BINARY)
    #     plt.imshow(masked_thr, cmap='gray')
    #     plt.title(i)
    #     plt.show()
        # cv2.imwrite("C:/Users/yjjeong/Desktop/paper/test.png", masked_thr)

        # plt.imshow(masked_thr, cmap='gray')
        # plt.show()

        # plt.imsave(f'./segment/{batch_idx}.png', outputs[0][0], cmap='gray')

# a = os.listdir('D:\macro_2023\predict_img')
a = glob.glob(r'D:\macro_2023\Pattern_recognition\predict_img/*.png')
# print(a[0])
# print(len(a))
# for i in range(len(a)):
#     print(a[i])
#     img = cv2.imread(a[i])
#     print(img)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # res, masked_thr = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    # plt.imshow(masked_thr, cmap='gray')
    # plt.show()

    # for i in range(0, 151, 5):
    #     res, masked_thr = cv2.threshold(img, i, 110, cv2.THRESH_BINARY)
    #     plt.imshow(masked_thr, cmap='gray')
    #     plt.title(i)
    #     plt.show()
