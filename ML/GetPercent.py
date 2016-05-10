import cv2
import numpy as np
import SetPreprocessing


def get_image_pixel_similarity(input_image):

    img1 = SetPreprocessing.set_preprocessing(input_image)
    img2 = cv2.imread('ref.png', 0)

    h, w = img2.shape[:2]

    height = range(h),
    width = range(w)

    diff_pixels = 0

    for i in height:
        for j in width:
            if(img1[i, j] != img2[i, j]):
                diff_pixels += 1

    tot_pix = h * w
    img_diff = (float(diff_pixels) * 10000) / (float(tot_pix) * 28.8896604938)

    return img_diff
