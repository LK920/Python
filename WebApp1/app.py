"""
date : 20/06/25
name : kang
content : python web programing
"""
#웹프로그래밍 설정파일
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello python Flask!!!</h1>'


@app.route('/hello')
def hello():
    return render_template('/hello.html')


if __name__ == '__main__':
    app.run()
