# FlaskTest

缺少一个config文件，可以根据自己实际需求填写config文件
   内容如下：
config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '密钥'
    PRICE_PER_PAGE = 5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    FLASKY_MAIL_SUBJECT_PREFIX = "帐号激活邮件:"
    FLASKY_MAIL_SENDER = "email"
    MAIL_SERVER = 'host'
    MAIL_PORT = port
    MAIL_USE_TLS = True
    MAIL_USERNAME = "username"
    MAIL_PASSWORD = 'password'
    MONGODB_SETTINGS = {
        'username': 'username',
        'password': 'password',
        'authMechanism': 'MONGODB-CR',
        'db': 'dbname',
        'host': 'host',
        'port': port
    }

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \ 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


