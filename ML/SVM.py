import cPickle
from ML import TransImage as ti
from ML import GetPercent as gp


class BSVM:
    def __init__(self):
        pass

    @staticmethod
    def get_bald_SVM(input_image):
        percent = gp.get_image_pixel_similarity(input_image)

        imgArr = ti.image_to_array(input_image)

        with open('learnData', 'rb') as f:
            clf = cPickle.load(f)

        type = int(clf.predict(imgArr))

        f.close()

        return {
            'result': {
                'PERCENT': percent,
                'TYPE': type
            }
        }