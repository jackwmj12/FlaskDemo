from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import Required,length,Email,EqualTo,Regexp
from werkzeug.security import generate_password_hash,check_password_hash
from ..models import User

class LoginForm(FlaskForm):
    username = StringField("登陆邮箱",validators=[Required(),Email(),length(1,64)])
    password = PasswordField("登陆密码",validators = [Required()])
    remember_me = BooleanField("保持登陆")
    submit_login = SubmitField("登陆")

class RegistrationForm(FlaskForm):
    email = StringField("登陆邮箱:",validators=[Required(),Email(),length(1,64)])
    username = StringField("用户   名:",validators=[Required(),length(1,64)])
    # Regexp("^[A-Za-z][A-Za-z-9_.]*$"), 0, "用户名只能包含字幕，数字，下划线，和点号"]
    password = PasswordField("输入密码:",validators=[Required(),EqualTo("password2",message="两次密码输入不相同")])
    password2 = PasswordField("再次输入:",validators=[Required()])
    submit_regist = SubmitField("注    册")

    def validate_email(self,field):
        if User.objects(email = field.data).first():
            raise ValidationError("该邮箱已被注册!!!")

    def validate_username(self,field):
        if User.objects(username = field.data).first():
            raise ValidationError("该用户名已被注册!!!")

class changePasswordForm(FlaskForm):
    # username = StringField("用户   名:", validators=[Required(), length(1, 64)])
    # Regexp("^[A-Za-z][A-Za-z-9_.]*$"), 0, "用户名只能包含字幕，数字，下划线，和点号"]
    oldpassword = PasswordField("输入原密码:", validators=[Required()])
    newpassword = PasswordField("输入新密码:", validators=[Required(),EqualTo("newpassword2", message="两次密码输入不相同")])
    newpassword2 = PasswordField("输入新密码:", validators=[Required()])
    submit_change = SubmitField("确定")