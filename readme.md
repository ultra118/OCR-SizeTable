# YOLO-v2 통한 size table detection

## [Darkflow](<https://github.com/thtrieu/darkflow>) 활용해 구현

- DarkNet이라는 딥러닝 프레임워크로 YOLO를 학습시키고 사용
- 이를 Python에서 사용하기위한 DarkFlow 사용

### 참조 링크

- [http://blog.ju-ing.com/2018/04/11/%EC%9E%90%EB%8F%99%EC%B0%A8-%EB%B2%88%ED%98%B8%ED%8C%90-%EC%9D%B8%EC%8B%9D-OCR-with-YOLO-v2/](http://blog.ju-ing.com/2018/04/11/자동차-번호판-인식-OCR-with-YOLO-v2/)

- [https://junyoung-jamong.github.io/deep/learning/2019/01/22/Darkflow%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%B4-YOLO%EB%AA%A8%EB%8D%B8-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%94%94%ED%85%8D%EC%85%98-%EA%B5%AC%ED%98%84-in-windows.html](https://junyoung-jamong.github.io/deep/learning/2019/01/22/Darkflow를-활용해-YOLO모델-이미지-디텍션-구현-in-windows.html)

## labelImg통해 학습 data set만들기

- pip install labelImg

### labelImg 사용

- `w` : 박스영역 생성
- `d` : 다음 이미지로 넘어가기
- `a` : 이전 이미지로 넘어가기
- labeling하는 폴더영역으로부터 각 이미지에대한 rect영역 설정하고 class로 분류
- size table인지 아닌지에 대한 object의 비율을 맞춰가며 `0`(non sizetable) `1`(size table) label 지정
- 한 이미지에 대한 `.xml`파일을 생성해가도록 한다

## install darkflow

- darkflow는 dartnet의 tensorflow 버전

```bash
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
python setup.py build_ext --inplace
pip install .
```

- not module cython이 뜨면

  ```bash
  pip install --upgrade cython
  ```

- Microsoft Visaul C++ 14.0 is required ERROR가 뜨면

  - [visual studio 2017 download](<https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15>)
    - version은 2017로 해서 됐기 때문에
  - 워크로드의 C++를 사용한 데스크톱 개발을 반드시 check
    - ![image](https://user-images.githubusercontent.com/28910538/58688526-b0389080-83bf-11e9-80af-54e69321c562.png)

- flow 명령어가 안되면 python flow로 쓰면 됨

## .cfg 설정

- darkflow/cfg/ 경로안의 yolo.cfg파일을 다른이름으로 저장하고 cfgㅇ을 만듬

```bash
[convolutional]
size=1
stride=1
pad=1
filters=35  #### (classes + 5) * 5
activation=linear


[region]
anchors =  0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828
bias_match=1
classes=2  #### 분류되는 classes 수와
coords=4
num=5
softmax=1
jitter=.3
rescore=1
```



## Training

```bash
python flow --model ./cfg/size-yolo.cfg --labels \
./labels.txt --trainer adam \
--dataset ../data/dataset/ --annotation ../data/annotations/ --train \
--summary ./logs --batch 5 --epoch 100 --save 50 --keep 5 --lr 1e-04 --gpu 0.5
```

- 아직 잘 모름 링크 참조
- gpu memory 뻑나면 그냥 --gpu 부분 지우고 cpu로 학습

## Predict

```bash
python flow --imgdir ../data/dataset/ --model ./cfg/size-yolo.cfg --load -1 \
--batch 1 --threshold 1.5 
```

- --imgdir 뒤에는 predict하는 이미지 폴더 경로
- --model은 사용되는 cfg의 경로
- 아직 잘 모름 링크 참조