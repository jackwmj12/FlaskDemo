from flask import render_template,redirect,url_for,session,request,flash
from . import main
from flask_login import login_required,login_user,logout_user
from ..auth.forms import LoginForm
from ..models import User

@main.route("/index")
@main.route("/")
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

@main.route("/main")
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

@main.route("/product")
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

@main.route("/download")
@login_required
def download():
    content = {
        "username": "",
        "password": "",
        "age": "",
        "gender": "",
    }
    return render_template("download.html",**content)

@main.route("/about")
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

@main.route("/login",methods = ["GET","POST"])
def login_menu():
    content = {
        "username": "",
        "password": "",}
    form = LoginForm()  # 创建表单对象
    if form.validate_on_submit():  # 如果表单提交
        user = User.objects(username= form.username.data).first()#从数据库获取相应用户信息
        if user is not None and user.verify_password(form.password.data):#验证密码
            print("登陆成功")
            login_user(user,form.remember_me.data)#登陆用户
            return redirect(request.args.get("next") or url_for("main.index"))#重定向链接
        flash("用户名或密码错误")#用户名密码错误
    import datetime
    content["username"] = form.username.data
    return render_template("login.html", form=form, current_time=datetime.datetime.utcnow())

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login_menu'))


@main.route("/alert")
def alert():
    return render_template("alert.html")

