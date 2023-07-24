# 필요한 모듈 import 
from flask import Blueprint, request, render_template, flash, redirect, url_for, request, send_file
from flask import current_app as app
from werkzeug.utils import secure_filename
import os, shutil, time
 
main = Blueprint('main', __name__, url_prefix='/')

# main 페이지
@main.route('/main', methods=['GET'])
def index():
      return render_template('/main/index.html')


#여기에서 파일 불러와서 해결하는 거 먼저 하고 넘어가자.
@main.route('/main/test', methods=['GET', 'POST'])
def process():
      if request.method=='POST':
            
            DATA_PATH = '/home/ubuntu/hs/mobility/'
            SAVE_PATH = '/home/ubuntu/hs/mobility/uploaded_file/' # 저장 경로
            
            if os.path.isdir(SAVE_PATH):
                  shutil.rmtree(SAVE_PATH) # 폴더가 비어있지 않으면 파일 모두 삭제
                  shutil.rmtree(DATA_PATH + 'runs/detect/')
                  os.mkdir(SAVE_PATH) # 폴더가 없으면 새로 생성
                  os.mkdir(DATA_PATH + 'runs/detect/')
            else:
                  os.mkdir(SAVE_PATH) # 폴더가 없으면 새로 생성
                  os.mkdir(DATA_PATH + 'runs/detect/')
            try:
                  f = request.files['file']
                  f.save(SAVE_PATH + secure_filename(f.filename))
                  import time
                  time.sleep(3)
                  return render_template('/main/process.html')
            except:
                  return render_template('/main/process.html')
                  
      return render_template('/main/process.html')


# detection 페이지
@main.route('/main/detect', methods=['GET', 'POST'])
def detect():
      import os
      import shutil
      import numpy as np
      
      if request.method == 'POST':
            DATA_PATH = '/home/ubuntu/hs/mobility/'
            SAVE_PATH = '/home/ubuntu/hs/mobility/uploaded_file/' # 저장 경로

            # Yolo 모델 불러오기
            from ultralytics import YOLO
            model = YOLO(DATA_PATH + 'best_0.75.pt')

            button_name = request.form.get('button')
            
            if os.path.isdir(SAVE_PATH):
                  shutil.rmtree(SAVE_PATH) # 폴더가 비어있지 않으면 파일 모두 삭제
                  shutil.rmtree(DATA_PATH + 'runs/detect/')
                  os.mkdir(SAVE_PATH) # 폴더가 없으면 새로 생성
                  os.mkdir(DATA_PATH + 'runs/detect/')
            else:
                  os.mkdir(SAVE_PATH) # 폴더가 없으면 새로 생성
                  os.mkdir(DATA_PATH + 'runs/detect/')
                  
            try:
                  f = request.files['file']
                  # 저장할 경로 + 파일명
                  f.save(SAVE_PATH + secure_filename(f.filename))
                  
                  class_name_dict = {0: '정상', 1: '보행자도로 통행 위반', 2: '동승자 탑승 위반', 3: '안전모 미착용 위반', 4: '무단횡단 위반', 
                                   5: '횡단보도 주행 위반', 6: '신호 위반', 7: '정지선 위반'}
                  # 결과 전달
                  vio_list = []
                  
                  if button_name == '이미지 객체탐지/초기화':
                        success_msg = 'image_file'

                        if '.jpg' not in f.filename and '.png' not in f.filename and '.jpeg' not in f.filename:
                              success_msg = 'not_correct_format'
                              return render_template('/main/detect.html', success_msg = success_msg)
                        results = model.predict(source= SAVE_PATH + f.filename, save = True)
                                                
                        for result in results:        
                        # confidence가 0.6이상인 클래스만 저장하도록.
                              uniq, cnt = np.unique(result.boxes.cls.cpu().numpy().astype(int)[np.where(result.boxes.conf.cpu().numpy() >= 0.6)], return_counts=True)  # Torch.Tensor -> numpy
                              uniq_cnt_dict = dict(zip(uniq, cnt))

                              vio_list.append(f'위반 유형 번호 : 유형별 위반 갯수 = {uniq_cnt_dict}')

                              for c in uniq_cnt_dict.keys():
                                    vio_list.append(f'위반 유형 번호 = {c}, 위반 유형 이름 = {class_name_dict[c]}')
                              
                              violation_cnt = sum([val for key, val in uniq_cnt_dict.items() if key != 0])
                              vio_list.append(f'총 {violation_cnt}건의 위반 사례가 있습니다.') 
                  
                  elif button_name == '비디오 객체탐지/초기화':
                        success_msg = 'video_file'
                        
                        if '.mp4' not in f.filename and '.avi' not in f.filename and '.mov' not in f.filename:
                              success_msg = 'not_correct_format'
                              return render_template('/main/detect.html', success_msg = success_msg)


                        results = model.predict(source= SAVE_PATH + f.filename, save = True)
                        video_pm_list = []

                        for i in range(8):
                              video_pm_list.append([i, 0])
                              pm_dict = dict(video_pm_list)

                        for result in results:        
                        # confidence가 0.6이상인 클래스만 저장하도록.
                              uniq, cnt = np.unique(result.boxes.cls.cpu().numpy().astype(int)[np.where(result.boxes.conf.cpu().numpy() >= 0.6)], return_counts=True)  # Torch.Tensor -> numpy
                              uniq_cnt_dict = dict(zip(uniq, cnt))
                              for key in uniq_cnt_dict.keys():
                                    pm_dict[key] += uniq_cnt_dict[key]
                        
                        if sum(pm_dict.values()) > 0:
                              vio_list.append('해당 영상에서는 다음과 같은 위반 사례가 존재합니다.')
                              for key, val in pm_dict.items():
                                    if val > 0 and key != 0:
                                          vio_list.append(class_name_dict[key])
                        else:
                              vio_list.append('해당 영상에서는 위반 사례가 존재하지 않습니다.')
                        os.system(f'ffmpeg -i {DATA_PATH}runs/detect/predict/{f.filename.split(".")[0] + ".avi"} -vcodec h264 {DATA_PATH}runs/detect/predict/{f.filename}')
                        
                  elif button_name == '비디오 파일 to H264 변환':
                        if '.mp4' not in f.filename:
                              success_msg = 'not_correct_format'
                              return render_template('/main/detect.html', success_msg = success_msg)
                        os.system(f'ffmpeg -i {SAVE_PATH + f.filename} -vcodec h264 {SAVE_PATH + "transformed_" + f.filename}')
                        return send_file(SAVE_PATH + "transformed_" + f.filename, as_attachment=True)
                  
                  else:
                        success_msg = ''
                  
                  return render_template('/main/detect.html', success_msg = success_msg, file_name = f.filename, vio_list = vio_list)

            except:
                  return render_template('/main/detect.html') 
      
      # 이미지 zip 파일을 입력해버리면 화면에 보여주지 말고 zip으로 압축해서 pred 결과를 돌려줘버리자.      

      return render_template('/main/detect.html')
      