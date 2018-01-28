from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,length,Email
from werkzeug.security import generate_password_hash,check_password_hash


class LoginForm(FlaskForm):
    username = StringField("登陆邮箱",validators=[Required(),Email(),length(1,64)])
    password = StringField("登陆密码",validators = [Required()])
    remember_me = BooleanField("保持登陆")
    submit_login = SubmitField("登陆")
    submit_register = SubmitField("注册")
    submit_logout = SubmitField("注销")


