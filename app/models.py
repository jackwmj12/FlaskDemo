from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
    username = StringField("What is your name?",validators=[Required()])
    password = StringField("Input your password",validators = [Required()])
    submit = SubmitField("Submit")