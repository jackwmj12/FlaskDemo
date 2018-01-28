from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import Required,length,Email,EqualTo,Regexp
from werkzeug.security import generate_password_hash,check_password_hash
from ..models import Oderawayequipments

class equipmentForm(FlaskForm):
	SerialNum = StringField("序列号",validators=[Required(),length(1,64)])
    # username = StringField("登陆邮箱",validators=[Required(),Email(),length(1,64)])
    # password = PasswordField("登陆密码",validators = [Required()])
    # remember_me = BooleanField("保持登陆")
