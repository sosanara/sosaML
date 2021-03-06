from ML import SVM
from ML import GetBinaryImage

input_image = '/img/2-1.png/'
reference_image = 'ref.png'
learnData = 'data/learnData/'

print SVM.BSVM.get_bald_SVM(input_image, reference_image, learnData)

binary_image = GetBinaryImage.BImage(input_image)
binary_image.save_binary_to_image('save', 1, 150, 120)

