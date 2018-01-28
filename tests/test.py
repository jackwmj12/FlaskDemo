from init import create_app,Manager,Migrate,db,MigrateCommand

app = create_app("default")
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command("db",MigrateCommand)

class User(db.Document):
    meta = {'collection': 'OderawayAccount'}
    username = db.StringField(unique = True)
    password_hash = db.StringField()
    phonenum = db.StringField()
    email = db.StringField(unique = True)
    confirmed = db.BooleanField(default = False)
    age = db.StringField()


if __name__=='__main__':
    manager.run()

# from flask import Flask
# from flask_script import Shell,Manager
# from flask_migrate import Migrate,MigrateCommand
# from flask_mongoengine import MongoEngine
# from config import config
# # from ..app.models import User
#
# db = MongoEngine()
#
# def create_app(config_name):#创建APP
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])  # 获取CONFIG
#     config[config_name].init_app(app)            # 初始化APP设置
#     db.init_app(app)                             # 初始化数据库
#     return app
#
# app = create_app("default")
# manager = Manager(app)
# migrate = Migrate(app,db)
# manager.add_command("db",MigrateCommand)
#
# if __name__=='__main__':
#     manager.run()
#
# # def make_shell_context(app,db):
# #     return dict(app = app,db = db,User = User,Role = Role)
#
# # manager.add_command("shell",Shell(make_shell_context))