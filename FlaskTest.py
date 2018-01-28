from flask import Flask,render_template,redirect,url_for,session
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from flask_mail import Message
from wtforms import StringField,SubmitField
from wtforms.validators import Required
import config

app = Flask(__name__)
app.config.from_object(config)
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
# app.config["SECRET_KEY"] = "hard to guess string"
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    username = StringField("What is your name?",validators=[Required()])
    password = StringField("Input your password",validators = [Required()])
    submit = SubmitField("Submit")

@app.route("/index")
@app.route("/")
def index():
    content = {
        "username":"LCC",
        "password":"123",
        "age":"15",
        "gender":"male",
        "frind":{
            "name":"SLS",
            "age":28,
            "gender":"fmale",
        }
    }
    return render_template("index.html",**content)

@app.route("/login")
def login():
    content = {
        "username": "LCC",
        "password": "123",
        "age": "15",
        "gender": "male",
        "frind": {
            "name": "SLS",
            "age": 28,
            "gender": "fmale",
        }
    }
    return render_template("login.html",**content)

@app.route("/main")
def main_menu():
    content = {
        "username": "LCC",
        "password": "123",
        "age": "15",
        "gender": "male",
        "frind": {
            "name": "SLS",
            "age": 28,
            "gender": "fmale",
        }
    }
    return render_template("main.html",**content)

@app.route("/product")
def product():
    content = {
        "username": "LCC",
        "password": "123",
        "age": "15",
        "gender": "male",
        "frind": {
            "name": "SLS",
            "age": 28,
            "gender": "fmale",
        }
    }
    return render_template("product.html",**content)

@app.route("/download")
def download():
    content = {
        "username": "LCC",
        "password": "123",
        "age": "15",
        "gender": "male",
        "frind": {
            "name": "SLS",
            "age": 28,
            "gender": "fmale",
        }
    }
    return render_template("download.html",**content)

@app.route("/about")
def about():
    content = {
        "username": "LCC",
        "password": "123",
        "age": "15",
        "gender": "male",
        "frind": {
            "name": "SLS",
            "age": 28,
            "gender": "fmale",
        }
    }
    return render_template("about.html",**content)

@app.route("/login")
def login_menu():
    content = {
        "username": "LCC",
        "password": "123",
        "age": "15",
        "gender": "male",
        "frind": {
            "name": "SLS",
            "age": 28,
            "gender": "fmale",
        }
    }
    return render_template("login.html",**content)

@app.route("/temp",methods = ["GET","POST"])
def temp_menu():
    content = {
        "username": "",
        "password": "",
        "age": "",
        "gender": "",
        "frind": {
            "name": "",
            "age": "",
            "gender": "",
        }
    }
    form = NameForm()                                                                                                   #创建表单对象
    if form.validate_on_submit():                                                                                           #如果表单提交
        session["username"]  = form.username.data                                                                       #用户名设置为表单内容
        session["password"] = form.password.data
        # se["username"] = form.username.data  # 用户名设置为表单内容
        # content["password"] = form.password.data
        return redirect(url_for("temp_menu"))
    import datetime
    content["username"] = session.get("username")
    content["password"] = session.get("password")
    return render_template("temp.html",**session,form = form,current_time=datetime.datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/alert")
def alert():
    return render_template("alert.html")

if __name__ == '__main__':
    app.run()
