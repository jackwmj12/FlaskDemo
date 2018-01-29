from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
login_manager = LoginManager()                  # 创建登陆管理
login_manager.session_protection = "strong"     # 设定保护等级
login_manager.login_view = "auth.login_menu"    # 添加登陆界面，放在view层
login_manager.login_message = "请先登陆您的帐号"
# login_manager.refresh_view = "accounts.reauthenticate"
# login_manager.needs_refresh_message = (
#     u"To protect your account, please reauthenticate to access this page."
# )
# login_manager.needs_refresh_message_category = "info"
db = MongoEngine()

def create_app(config_name):#创建APP
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 获取CONFIG
    config[config_name].init_app(app)            # 初始化APP设置
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)                  # 初始化登陆管理
    db.init_app(app)                             # 初始化数据库
    # attach routes and custom error pages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)       # 初始化蓝图
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = "/auth")
    # print(app.config["Login_Message"])
    return app
