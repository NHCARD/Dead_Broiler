import datetime
import sys
from func import find_download_pos
import cv2
from PIL import Image
import mss
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import pyautogui
from time import sleep

def dic_remove(name, result):
    for i in name:
        # print(i)
        while '' in result[i]:
            result[i].remove('')


    return result

def tesseract(bang_pos):
    try:
        cap_pos = (bang_pos[0] + 58, bang_pos[1] + 97, 239, 410)
    except TypeError:
        sys.exit(-1)

    a = pyautogui.screenshot(region=cap_pos)
    cvimg = np.array(a)

    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_RGB2BGR)
    cv2.imwrite('./cap_original.png', cvimg)

    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)
    cvimg = cv2.resize(cvimg, interpolation=cv2.INTER_LINEAR, dsize=(400, 664))

    result = pytesseract.image_to_data(cvimg, lang="kor+eng", output_type=pytesseract.Output.DICT)

    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_GRAY2BGR)
    for i in range(0, len(result["text"])):
        x = result["left"][i]
        y = result["top"][i]
        w = result["width"][i]
        h = result["height"][i]

        text = result["text"][i]
        conf = int(result["conf"][i])

        if conf > 70:
            text = "".join([c if ord(c) < 128 else "" for c in text])
            cv2.rectangle(cvimg, (x, y), (x + w, y + h), (0, 255, 0), 2)


    for i in range(len(result['text'])):
        if result['text'][i] == '':
            result['left'][i] = ''
            result['width'][i] = ''
            result['top'][i] = ''
            result['height'][i] = ''
            result['conf'][i] = ''

    result = dic_remove(['text', 'left', 'width', 'top', 'height', 'conf'], result)
    # print()

    # while '' in result['text']:
    #     result['text'].remove('')

    # print(result['text'])

    cv2.imwrite('./cv2_output.png', cvimg)

    return result


def find_pos(target):
    bang_pos = pyautogui.locateOnScreen('./bang!.png')
    pyautogui.moveTo(x=bang_pos[0] + 30, y=bang_pos[1] + 100, duration=0.5)
    sleep(0.5)
    while(True):
        time = []

        result = tesseract(bang_pos=bang_pos)
        print(result['left'])


        for i in result['text']:
            if len(i) < 5:
                continue
            elif i[:4] != '2023':
                time.append(i)

        pos_idx = find_download_pos(time, result, target)
        if pos_idx != None:
            break
        pyautogui.scroll(-320)

        print(result['left'])
    print(pos_idx)
    return [result['left'][pos_idx + 1], result['top'][pos_idx + 1]], bang_pos

# while(o):
#     for i in range(int(len(time)/2)):
#         atime = datetime.time.fromisoformat(time[0+i])
#         btime = datetime.time.fromisoformat(time[(int(len(time)/2))+i])
#         if atime < target < btime:
#             print('asdf')
#             break
#
#         for j in range(len(result['text'])):

#             if str(target) == result['text'][j]:
#                 print(result['left'][j])
#                 o = False
#                 break
#
#         pyautogui.scroll(-320)
