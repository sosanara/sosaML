import cv2
import numpy as np
import time
import SetPreprocessing
from PIL import Image


def image_to_array(input_image):
    img_arr = []
    im = Image.open(input_image).convert('L')
    width = im.size[1]
    height = im.size[0]

    pre_processing_image = SetPreprocessing.set_preprocessing(input_image)

    trans_image = cv2.resize(pre_processing_image, (height / 10, width / 10))
    ret, re_trans_image = cv2.threshold(trans_image, 127, 255, cv2.THRESH_BINARY)

    trans_width = range(7, 46)
    trans_height = range(18, 70)

    for i in trans_height:
        for j in trans_width:
            if re_trans_image[i, j] == 255:
                re_trans_image[i, j] = 1
            img_arr.append(re_trans_image[i, j])

    return img_arr

