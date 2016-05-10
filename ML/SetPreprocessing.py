import cv2
import numpy as np


def set_preprocessing(input_image):

    img = cv2.imread(input_image)
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Flesh Skin's Color ( Modify the Range )
    lower_skin = np.array([70, 137, 70])
    upper_skin = np.array([255, 180, 140])
    mask = cv2.inRange(img_YCrCb, lower_skin, upper_skin)

    return mask