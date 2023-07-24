from flask import Flask
from app.main.index import main as main

def create_app():
    app = Flask(__name__, static_folder = '/home/ubuntu/hs/mobility/') # 절대 경로로 설정해서 모든 파일의 접근에 용이하도록
    
    # index.py를 main page로 연동해줌 
    app.register_blueprint(main)
    return app