from flask import render_template,redirect,url_for,session,request,flash,current_app
from . import auth
from flask_login import login_required,login_user,logout_user
from .forms import LoginForm,RegistrationForm,changePasswordForm
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
        login_user(user)
        return redirect(url_for("main.index_menu"))
    return render_template("register.html",form = form)

@auth.route("/login",methods = ["GET","POST"])
def login_menu():
    content = {
        "username": "",
        "password": "", }
    form = LoginForm()  # 创建表单对象
    if form.validate_on_submit():  # 如果表单提交
        user = User.objects(email=form.username.data).first()  # 从数据库获取相应用户信息
        if user is not None and user.verify_password(form.password.data):  # 验证密码
            # login_user(user, form.remember_me.data)  # 登陆用户
            login_user(user)  # 登陆用
            return redirect(request.args.get("next") or url_for("main.index_menu"))  # 重定向链接
        flash("用户名或密码错误")  # 用户名密码错误
    import datetime
    content["username"] = form.username.data
    return render_template("login.html",form=form, current_time=datetime.datetime.utcnow())

@auth.route("/config",methods = ["GET","POST"])
def changePassword_menu():
    form = changePasswordForm()
    if form.validate_on_submit():
        user = User.objects(email=current_user.email).first()  # 从数据库获取相应用户信息
        if user.verify_password(form.oldpassword.data):
            if form.newpassword.data != form.newpassword2.data:
                flash("两次密码输入不一致")
            else:
                user.password_hash = form.newpassword.data
                user.commit()
            return redirect(url_for("main.index_menu"))
        else:
            flash("请输入正确的密码")
    return render_template("auth/changePassword.html", form=form)
        # user.password_hash =
    #     user.commit()
    #     token = user.generate_confirmation_token()
    #     send_email(user.email, "激活你的账户", "auth/email/confirm", user=user, token=token)
    #     login_user(user)
    #     return redirect(url_for("main.index_menu"))
    # return render_template("register.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    print("注销登陆")
    logout_user()#登出用户
    return redirect(url_for('auth.login_menu'))#返回主界面

@auth.route("/confirm/<token>")
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for("main.index_menu"))
    if current_user.confirm(token):
        flash("成功激活帐户，谢谢")
    else:
        flash("链接错误或者失效")
    return redirect(url_for("main.index_menu"))

@auth.route("/unconfirm")
@login_required
def unconfirm():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for("main/index_menu"))
	return render_template("auth/unconfirm.html")

@auth.route("/confirm")
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email,"请激活您的帐户","auth/email/confirm",user=current_user.username,token=token)
    flash("一封新的激活邮件正发送到您的邮箱.")
    return redirect(url_for("main.index_menu"))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != "auth." and request.endpoint != "static":
        return redirect(url_for("auth.unconfirm"))