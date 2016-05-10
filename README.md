#sosaML
<br></br>
##Installation
```sh
$ git clone https://github.com/sosanara/sosaML.git
```

##How to use :
#####if you not have **PIL**, **cv2**, **numpy**, **sklearn** library, you can first
```sh
$ pip install PIL
$ pip install numpy
$ brew install opencv
$ pip install sklearn
```
#####Example :
```sh
>>> from ML import SVM
>>> input_image = 'your/image/path.png'
>>> SVM.BSVM.get_bald_SVM(input_image) 
>>> gbi.BImage.get_binary_image(input_image, 'your/image/save/path', 'imageName')
```
<br></br>

##Result :
{'result': {'TYPE': 0~4, 'PERCENT': 0.0~100.0}}
<br></br>

##File description :
####1) GetPercent.py

#####def get_image_pixel_similarity(input_image)

input_image : 사용자가 보낸 머리 이미지(540*960)

return : 전체 원 안의 살색의 비율

<br></br>
####2) SetPreprocessing.py

#####def set_preprocessing(input_image)

input_image : 사용자가 보낸 머리 이미지(540*960)

return : 살색은 흰색, 나머지는 검은색으로 이진화 된 이미지.

<br></br>
####3) TransImage.py

#####def image_to_array(input_image)

input_image : 사용자가 보낸 머리 이미지(540*960)

return : 이미지 이진화 시켜 배열로 저장한 배열값

<br></br>
####4) SVM.py

#####def get_bald_SVM(input_image)

input_image : 사용자가 보낸 머리 이미지(540*960)  
  
return : SVM을 이용한 결과타입 및 퍼센트 값
  
<br></br>
####5) GetBinaryImage.py

def get_binary_image(input_image, path, fname='skin_color')

input_image : 사용자가 보낸 머리 이미지(540*960) 

path : 이진화된 이미지를 저장하고 싶은 위치 

fname='skin_color' : 저장할 이미지의 이름(default = 'skin_color.png')

실행결과 : skin color를 추출한 이진화이미지가 path경로에 저장된다.

<br></br>
####6) MakeData.py

데이터가 있는 csv파일을 서버에서 사용할 수 있도록 미리 학습시켜놓은 후 저장한다.
