from PIL import Image
from Preprocessing import Preprocessing
import cv2


class BImage:
    input_image = None
    binary_image = None
    image_name = None
    path = None

    def __init__(self, input_image):
        self.input_image = Preprocessing.remove_slash(input_image)
        self.binary_image = Preprocessing.detect_skin_color(input_image)
        self.image_name = self._image_name(self.input_image)

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

    def _image_background(self, img_name, bgr_choice, bgr_compare, bgr_value):
        change_convert_image = Image.open(img_name).convert('RGB')
        img = cv2.imread(self.input_image)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j][bgr_choice] > bgr_compare:
                    change_convert_image.putpixel((j, i), bgr_value)
        change_convert_image.save(img_name, "PNG")

    def save_binary_to_image(self, path, bgr_choice, bgr_compare, bgr_value):
        path = Preprocessing.append_slash(path)
        img_name = path + 'binary_' + self.image_name + '.png'
        cv2.imwrite(img_name, self.binary_image)
        self._image_background(img_name, bgr_choice, bgr_compare, bgr_value)

        return {
            'filename': 'binary_' + self.image_name,
            'path': path,
            'fullname': img_name
        }
