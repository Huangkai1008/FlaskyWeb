from flask import Flask
from flask_script import Manager
# from flask import request
# from flask import make_response
# from flask import redirect
# from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


# # 请求上下文
# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent
#
#
# # 状态码
# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400
#
#
# # make_response函数
# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', 42)
#     return response
#
#
# # 重定向函数
# @app.route('/')
# def index():
#     return redirect('http://www.example.com')

# Flask_Script
manager = Manager(app)

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    manager.run()