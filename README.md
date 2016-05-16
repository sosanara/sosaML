# sosaML
---

## Installation
```sh
$ git clone https://github.com/sosanara/sosaML.git
```

## How to use :
#### if you not have **PIL**, **cv2**, **numpy**, **sklearn** library, you can first
```sh
$ pip install pillow
$ pip install numpy
$ pip install scipy
$ pip install sklearn
```
#### Example :
```python
from ML import SVM
from ML import GetBinaryImage

input_image = 'img/2.png/'
reference_image = 'ref.png'
learnData = 'data/learnData/'

binary_image = GetBinaryImage.BImage(input_image)
binary_image.save_binary_to_image('save')

print SVM.BSVM.get_bald_SVM(input_image, reference_image, learnData)
```
<br></br>

##Result :
```javascript
{'result': {'type': 0~4, 'percent': 0.0~100.0}}
```

## File description (Class units):

#### 1) Preprocessing.py

```python
@staticmethod
def append_slash(path)
```
path : path 끝에 '/'가 있는 지 확인 후 추가

return : 경로

```python
@staticmethod
def remove_slash(path)
```
path : path 끝에 '/'가 있는 지 확인 후 제거

return : 경로

```python
@staticmethod
def detect_skin_color(input_image)
```
input_image : 사용자 머리 이미지 경로

return : 머리 이미지의 binary 이미지 값

```python
def image_to_array(self)
```
return : binary 이미지 값을 배열로 전환한 값

```python
def get_image_pixel_similarity(self)
```
return : Reference 이미지와 input 이미지의 차이 % (얼마나 다른지)

#### 2) GetBinaryImage.py

```python
def _image_name(self, input_image))
````
input_image : 사용자 머리 이미지 경로

return : 이미지 파일 이름

```python
def _image_background(self, img_name, bgr_choice, bgr_compare_up, bgr_compare_down, bgr_value)
```
img_name : 이진화된 이미지

bgr_choice : bgr 중 컬러 선택

bgr_compare_up : bgr_choice 에서 고른 색을 비교할 값

bgr_compare_down : bgr_choice 에서 고른 색을 제외하고 비교할 값

bgr_value : 조건을 만족하면 넣을 value (tuple rgb 값)

이미지의 테두리의 색을 바꿔서 저장

```python
def save_binary_to_image(self, path)
```
input_image : 사용자 머리 이미지 경로

머리 이미지의 살색 검출 후, binary로 바꾼 값을 이미지로 저장

####3) SVM.py

```python
@staticmethod
def get_bald_SVM(input_image, reference_image, learn_data)
```

input_image : 사용자 머리 이미지 경로

reference_image : 비교할 머리 기준 이미지

learn_data : 학습시켜 놓은 파일
