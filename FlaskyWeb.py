from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail

# from flask import request
# from flask import make_response
# from flask import redirect
# from flask import abort

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 设置密钥
app.config['SECRET_KEY'] = 'hard to guess string'
# 设置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:177036@localhost:3306/FlaskyWeb?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 设置qq邮箱
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


@app.route('/', methods=['GET', 'POST'])
def index():
    # 实现重定向和用户会话
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['Known'] = False
        else:
            session['Known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

    # name = None
    # form = NameForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''
    # return render_template('index.html', form=form, name=name)


# SqlAlchemy
db = SQLAlchemy(app)


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


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


"""
数据库模型
"""


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


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

# Flask_Mail
mail = Mail(app)


# 集成python shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("Shell", Shell(make_context=make_shell_context()))

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    manager.run()
