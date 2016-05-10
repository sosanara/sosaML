import os

from ML import SVM
from ML import GetBinaryImage as gbi

input_image = 'img/your_image.png'

gbi.BImage.get_binary_image(input_image, 'your/image/save/path', 'imageName')

print SVM.BSVM.get_bald_SVM(input_image)