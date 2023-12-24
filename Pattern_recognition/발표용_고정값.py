import os

import pyautogui
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from temp2 import predict
from b_box import find_pos
import time
import cv2
import datetime


def vid_img(vid, person_time):
    person_time = datetime.time.fromisoformat(person_time)  # 실제로는 욜로로 탐지한 시간 기입 - n_time
    # print(vid[0][-14:-16])

    vid_stime = vid[0][-10:-8] + ':' + vid[0][-8:-6] + ':' + vid[0][-6:-4]
    # print(vid_stime)
    vid_stime = datetime.time.fromisoformat(vid_stime)
    # print(vid_stime)
    time_interval = (datetime.timedelta(hours=person_time.hour, minutes=person_time.minute, seconds=person_time.second) \
                     - datetime.timedelta(hours=vid_stime.hour, minutes=vid_stime.minute,
                                          seconds=vid_stime.second)).total_seconds()
    print(time_interval)

    try:
        os.mkdir(f'/vid_cut-Img/{vid[0][:-4]}')
    except:
        pass

    for j in range(int(time_interval - 30), int(time_interval + 31), 2):
        os.system(
            fr"ffmpeg -vsync 2 -ss {j} -t {j + 1} -i {'./vid' + '/' + vid[0]} -an -vf thumbnail=20 ./vid_cut-img\{vid[0][:-4]}\{vid[0][:-4]}_{j}.png")

def run():
    ch, n_time = predict()
    time.sleep(2)
    pyautogui.hotkey('esc')
    time.sleep(0.5)

    # pyautogui.moveTo()
    pyautogui.click(pyautogui.locateOnScreen('./search.png'), duration=1)
    pyautogui.click(pyautogui.locateOnScreen('./download.png'), duration=1)
    time.sleep(0.3)

    print(n_time.hour, n_time.minute, n_time.second)
    pos, bang_pos = find_pos([n_time.hour, n_time.minute, n_time.second])
    pyautogui.moveTo(x=pos[0] + bang_pos[0] - 53, y=pos[1] + bang_pos[1] + 115, duration=1)
    pyautogui.click()
    pyautogui.click(pyautogui.locateOnScreen('./download_btn.png'), duration=0.5)
    pyautogui.click(pyautogui.locateOnScreen('./download_stop.png'), duration=0.5)

    # 7 : 40 : 01

    vid = os.listdir('./vid')

    person_time = datetime.time.fromisoformat('13:25:08')  # 실제로는 욜로로 탐지한 시간 기입 - n_time
    # print(vid[0][-14:-16])

    vid_stime = vid[0][-10:-8] + ':' + vid[0][-8:-6] + ':' + vid[0][-6:-4]
    # print(vid_stime)
    vid_stime = datetime.time.fromisoformat(vid_stime)
    # print(vid_stime)
    time_interval = (datetime.timedelta(hours=person_time.hour, minutes=person_time.minute, seconds=person_time.second) \
                     - datetime.timedelta(hours=vid_stime.hour, minutes=vid_stime.minute,
                                          seconds=vid_stime.second)).total_seconds()
    print(time_interval)

    try:
        os.mkdir(f'./vid_cut-Img/{vid[0][:-4]}')
    except:
        pass

    for j in range(int(time_interval - 30), int(time_interval + 31), 2):
        os.system(
            fr"ffmpeg -vsync 2 -ss {j} -t {j + 1} -i {'./vid' + '/' + vid[0]} -an -vf thumbnail=20 ./vid_cut-img\{vid[0][:-4]}\{vid[0][:-4]}_{j}.png")

    # print(ch)
    # print(time)


if __name__ == "__main__":
    # run()
    vid_img(list([r"0_8_IPC3_20221107132359.mp4"]), '13:25:08')
