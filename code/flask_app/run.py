from flask import Flask
from app import create_app # app vhfejdml init 파일에서 create_app함수 가져오기

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)