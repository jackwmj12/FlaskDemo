from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

def create_app(config_name):#创建APP
    app = Flask(__name__)
    app.config.from_object(config[config_name])#获取CONFIG
    config[config_name].init_app(app)#初始化APP设置
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    # db.init_app(app)
    # attach routes and custom error pages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
