from flask_login import UserMixin
from .import login_manager
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id = user_id).first()

class User(UserMixin,db.Document):
    meta = {'collection': 'TestAccount'}
    username = db.StringField(unique = True)
    password_hash = db.StringField()
    phonenum = db.StringField()
    email = db.StringField(unique = True)
    confirmed = db.BooleanField(default = False)

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")

    @password.setter                                                                        # 当password设置时，触发以下函数
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return False

    def is_anonymous(self):
        return False

    def verify_password(self, password):
        return check_password_hash(self.password_hash,str(password))                        # 返回检查结果

    def __repr__(self):
        return '<User %r>' % self.username                                                  # 返回username

    def commit(self):
        self.password = self.password_hash                                                  # 赋值password,触发self.password_hash = generate_password_hash(password=password)
        self.save()                                                                         # 提交账户信息

    def generate_confirmation_token(self, expiration=3600): # 生成注册确认令牌，默认一小时有效
        s = Serializer(current_app.config["SECRET_KEY"],expiration)
        return s.dumps({"confirm":int("0x{}".format(str(self.id)),16)})

    def confirm(self,token):# 验证注册令牌，验证通过则把confirmed属性设为True
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data  = s.loads(token)
        except Exception as e:
            print("User Confirm Error:{}".format(e))
            return False
        if data.get("confirm") !=int("0x{}".format(str(self.id)),16):
            return False
        self.confirmed = True
        self.save()
        return True

class OderawayStatus(db.Document):
    meta = {'collection': '',
            'ordering': ['Time']}
    WorkFre = db.StringField()
    NH3 = db.StringField()
    WorkStatus = db.StringField()
    LiquidNum = db.BooleanField()
    LiquidMargin = db.StringField()
    Time = db.StringField()
    WarningInfo = db.StringField()

    @staticmethod
    def objectsByser(self,ser_num):
        self.meta = {'collection': '{}'.format(ser_num),
            'ordering': ['Time']}
        return self.objects

class PriceInfo(db.Document):
    meta = {'collection': 'price_info',
            'ordering': ['date']}
    num = db.StringField()
    index = db.StringField()
    url = db.StringField()
    date = db.StringField()
    coper_price = db.StringField()
    coper_changed = db.StringField()
    aluminium_price = db.StringField()
    aluminium_changed = db.StringField()

    def to_dict(self):
        return {
            'index': self.index,
            'url': self.url,
            'date': self.date,
            'coper_price': self.coper_price,
            'coper_changed': self.coper_changed,
            'aluminium_price': self.aluminium_price,
            'aluminium_changed': self.aluminium_changed,}


class Ip(db.Document):
    meta = {'collection': 'ip'}
    index = db.StringField()
    name = db.StringField()
    ip = db.StringField()
    num = db.BooleanField()




