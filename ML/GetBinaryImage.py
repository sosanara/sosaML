from Preprocessing import Preprocessing
import cv2


class BImage:
    binary_image = None
    image_name = None
    path = None

    def __init__(self, input_image):
        self.binary_image = Preprocessing.detect_skin_color(input_image)
        self.image_name = self._image_name(Preprocessing.remove_slash(input_image))

    def _image_name(self, input_image):
        temp = input_image.split('/')[-1]
        if temp.find('.png') != -1: return temp.split('.png')[0]
        elif temp.find('.PNG') != -1: return temp.split('.PNG')[0]
        elif temp.find('.jpg') != -1: return temp.split('.jpg')[0]
        elif temp.find('.JPG') != -1: return temp.split('.JPG')[0]
        elif temp.find('.jpeg') != -1: return temp.split('.jpeg')[0]
        elif temp.find('.JPEG') != -1: return temp.split('.JPEG')[0]
        elif temp.find('.bmp') != -1: return temp.split('.bmp')[0]
        elif temp.find('.BMP') != -1: return temp.split('.BMP')[0]

    def save_binary_to_image(self, path):
        path = Preprocessing.append_slash(path)
        img_name = path + 'binary_' + self.image_name + '.png'
        cv2.imwrite(img_name, self.binary_image)
