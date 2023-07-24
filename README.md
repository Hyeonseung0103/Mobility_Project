# 개인형 이동장치의 교통법 위반 유형 탐지

오토바이, 자전거, 킥보드와 같은 개인형 이동장치의 교통법 위반 유형 탐지를 위한 Object Detection 모델 개발을 주제로 진행한 프로젝트이다. 개인으로 진행했고, 데이터 수집, EDA 및 데이터 전처리, 모델링, 서비스 구현 등의 역할을 수행했다.

[프로젝트 내용 설명 영상](https://drive.google.com/file/d/1mDt51ca6Zd5PS2JLJXFw_QcU8b4RV_Om/view?usp=sharing)

## ## 프로젝트 개요 및 필요성
- 오늘날 많은 사람들이 카카오 바이크, 지쿠터와 같은 개인형 이동수단을 이용하는만큼 발생하는 교통사고 건수도 해마다 증가하고 있는 추세다. 아래 그래프를 보면 알 수 있듯이 2021년에는 2017년에 보다 약 15배 이상이 되는 개인형이동수단 교통사고 건수를 기록하고 있다. 

<br><br><br>
<p align="center">

<img src="https://github.com/Hyeonseung0103/Mobility_Project/assets/97672187/a9e7b9ea-b371-42df-986b-689a79616ea1" width="40%" height="40%">

<br>

- AI 모델이 위법 사항들을 자동으로 빠르게 탐지하여 바로 벌금을 부과하는 등의 처벌이 이루어진다면 사고를 발생시키는 이용자는 최대한 위법을 하지 않으려고 노력할 것이고, 교통사고가 사전에 예방되어 사고건수를 줄일 수 있다. 사고의 피해자가 될 수 있는 보행자 및 차량의 입장에서는 위험 요소가 사라져 안전하게 보행 혹은 주행을 할 수 있다는 안정성이 생길 것이고, 교통사고 발생시 사고현장을 처리하고 사고 정도에 따라 여러 인적 자원이 투입되어야 하는 경찰의 입장에서는 사고처리를 위한 비용과 이동수단 단속을 위한 인적 자원을 다른 현장에 사용할 수 있게 될 것이다.

- 본 프로젝트는 위와 같은 기대효과에 달성하기위해 개인형 이동장치(오토바이, 자전거, 킥보드)의 교통법 위반 유형을 탐지하는 Object Detection 모델을 개발했다.

- 목표: 개인형 이동장치의 위법사례로 인해 경찰, 이용자, 보행자 및 차량에게 발생할 수 있는 위험/불편한 요인들을 최소화 할 수 있도록 0.7이상의 MAP 50 Score를 기록하는 준수한 모델을 만들고, 해당 모델을 사용하여 실제로 개인형 이동장치의 교통법 위반 사례를 분류할 수 있는 웹페이지 형태의 서비스를 제공한다.



## 프로젝트 파이프라인
1. 데이터는 AI-Hub에서 제공.
2. 제공 받은 데이터는 파이썬과 Open CV 라이브러리를 활용해 전처리(640 x 640으로 사이즈 변환, 흑백 이미지로 변환).
3. 딥러닝 프레임워크 중 하나인 Pytorch 기반의 Yolov5s, Yolov8n 모델 사용.
4. Flask를 활용하여 최종 모델을 실제로 사용해 볼 수 있도록 웹페이지 형태의 서비스 구현.

<img width="1205" alt="image" src="https://github.com/Hyeonseung0103/Mobility_Project/assets/97672187/a6c7dff4-1897-436b-9c66-277dbfb253a5">

## 데이터 설명
- 수집 및 모델에 사용한 데이터: AI-Hub 사이트 제공(약 16,000개)

- 학습 데이터: 10,500개
- 검증 데이터: 2,500개
- 테스트 데이터: 3,000개
- 데이터 용량: 약 13GB
- 원본 이미지/라벨 이미지

<img width="490" alt="image" src="https://github.com/Hyeonseung0103/Mobility_Project/assets/97672187/1dd134ee-e6cc-4250-999d-5a82b637501c">
<img width="500" alt="image" src="https://github.com/Hyeonseung0103/Mobility_Project/assets/97672187/a56aaeff-f075-4b1d-862e-ea8b4de95e21">


## 모델링


### 1. 사용한 모델


### 2. 성능



## 결론



## 한계점 및 해결방안




