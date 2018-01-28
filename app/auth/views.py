from flask import render_template,redirect,url_for,session,request,flash,current_app
from . import auth
from flask_login import login_required,login_user,logout_user
from .forms import LoginForm,RegistrationForm
from ..models import User
from ..email import send_email
from flask_login import current_user


@auth.route('/register',methods = ["GET","POST"])
def register_menu():
    form = RegistrationForm()#初始化注册表单
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,password_hash = form.password.data)
        user.commit()
        token = user.generate_confirmation_token()
        send_email(user.email,"激活你的账户","auth/email/confirm",user=user,token=token)
        flash("尊敬的用户，激活链接已发送至您的邮箱:{}".format(user.email))
        return redirect(url_for("auth.login_menu"))
    return render_template("register.html",form = form)

@auth.route("/login",methods = ["GET","POST"])
def login_menu():
    content = {
        "username": "",
        "password": "",}
    form = LoginForm()  # 创建表单对象
    if form.validate_on_submit():  # 如果表单提交
        user = User.objects(email = form.username.data).first()#从数据库获取相应用户信息
        if user is not None and user.verify_password(form.password.data):#验证密码
            login_user(user,form.remember_me.data)#登陆用户
            return redirect(request.args.get("next") or url_for("main.index"))#重定向链接
        flash("用户名或密码错误")#用户名密码错误
    import datetime
    content["username"] = form.username.data
    return render_template("login.html", form=form, current_time=datetime.datetime.utcnow())

@auth.route('/logout')
@login_required
def logout():
    logout_user()#登出用户
    return redirect(url_for('auth.login_menu'))#返回主界面

@auth.route("/confirm/<token>")
@login_required
def confirm(token):
    print("激活活动已发起")
    if current_user.confirmed:
        print("当前账户已经被激活")
        return redirect(url_for("main.index"))
    if current_user.confirm(token):
        print("成功激活帐户，谢谢")
        flash("成功激活帐户，谢谢")
    else:
        print("链接错误或者失效")
        flash("链接错误或者失效")
    return redirect(url_for("main.index"))

@auth.before_app_request
def before_request():
    pass
    # print("************************************")
    # return None
    # if current_user.is_authenticated is True and current_user.confirmed is False:
    #     print("重定向")
    #     return redirect(url_for("auth.unconfirmed"))
#
@auth.route("/unconfirmed")
def unconfirmed():
    if current_user.is_anymous() or current_user.confirmed:
        return redirect(url_for("main.index"))
    return render_template("auth/unconfirmed.html")


@auth.route("/confirm")
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email,"Confirm Your Account","auth/email/confirm",user=current_user,token=token)
    flash("A new confirmation email has been sent to you by email.")
    return redirect(url_for("main.index"))