import cPickle
from SetPreprocessing import set_preprocessing as sp
import cv2


class BImage:

    @staticmethod
    def get_binary_image(input_image, path, fname='skin_color'):
        binary_image = sp(input_image)
    
        img_name = path + '\\'+ fname +'.png'
        cv2.imwrite(img_name, binary_image)