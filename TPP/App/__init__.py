from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    # url格式：数据库+驱动//用户名：密码@主机：端口号/具体哪一个库
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:password@localhost:3307/flaskdb"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_api(app=app)
    return app



