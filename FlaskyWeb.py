from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
# from flask import request
# from flask import make_response
# from flask import redirect
# from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 自定义错误界面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



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

# Flask_BootStrap
bootstrap = Bootstrap(app)

# Flask_Moment
moment = Moment(app)

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    manager.run()

