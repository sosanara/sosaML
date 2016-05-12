import cPickle
from Preprocessing import Preprocessing


class BSVM:
    @staticmethod
    def get_bald_SVM(input_image, reference_image, learn_data):
        pre = Preprocessing(input_image, reference_image)
        percent = pre.pixel_similarity()
        imgArr = pre.image_to_array()

        with open(Preprocessing.remove_slash(learn_data), 'rb') as f:
            clf = cPickle.load(f)

        type = int(clf.predict(imgArr))

        f.close()

        return {
            'result': {
                'PERCENT': percent,
                'TYPE': type
            }
        }
