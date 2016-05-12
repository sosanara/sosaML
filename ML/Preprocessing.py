import cv2
import numpy
from PIL import Image


class Preprocessing:
    input_image = None
    reference_image = None

    def __init__(self, input_image, reference_image):
        self.input_image = self.remove_slash(input_image)
        self.reference_image = self.remove_slash(reference_image)

    @staticmethod
    def append_slash(path):
        if path[-1] != '/':
            return path + '/'
        return path

    @staticmethod
    def remove_slash(path):
        if path[-1] == '/':
            return path[:len(path)-1]
        return path

    @staticmethod
    def detect_skin_color(input_image):
        input_image = Preprocessing.remove_slash(input_image)
        img = cv2.imread(input_image)
        img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

        # Flesh Skin's Color ( Modify the Range )
        lower_skin, upper_skin = numpy.array([70, 137, 70]), numpy.array([255, 180, 140])
        skin = cv2.inRange(img_YCrCb, lower_skin, upper_skin)

        return skin

    def image_to_array(self):
        img_arr = []
        im = Image.open(self.input_image).convert('L')
        width, height = im.size[0], im.size[1]

        skin_color = self.detect_skin_color(self.input_image)

        trans_image = cv2.resize(skin_color, (width / 10, height / 10))
        ret, re_trans_image = cv2.threshold(trans_image, 127, 255, cv2.THRESH_BINARY)

        trans_width, trans_height = range(7, 46), range(18, 70)

        for i in trans_height:
            for j in trans_width:
                if re_trans_image[i, j] == 255:
                    re_trans_image[i, j] = 1
                img_arr.append(re_trans_image[i, j])

        return img_arr

    def pixel_similarity(self):

        img1 = self.detect_skin_color(self.input_image)
        img2 = cv2.imread(self.reference_image, 0)

        h, w = img2.shape[:2]
        height, width = range(h), range(w)
        diff_pixels = 0

        for i in height:
            for j in width:
                if img1[i, j] != img2[i, j]:
                    diff_pixels += 1
        tot_pix = h * w

        return (float(diff_pixels) * 10000) / (float(tot_pix) * 28.8896604938)
