from flask import render_template,redirect,url_for,session,request,flash,current_app
from sqlalchemy.sql.functions import user

from . import main
from flask_login import login_required, current_user
from ..models import OderawayStatus,Ip,PriceInfo,User,Oderawayequipments
from flask import jsonify

@main.route("/index")
@main.route("/")
def index_menu():
	if not current_user.is_anonymous:
		if not current_user.confirmed:
			flash("尊敬的用户，激活链接已发送至您的邮箱:{},登陆后，请点击发进您邮箱内的链接进行激活，谢谢".format(current_user.email))
	return render_template("index.html")

@main.route("/main")
def main_menu():
    return render_template("main.html")

@main.route("/product")
def product():
    return render_template("product.html")

@main.route("/download")
@login_required
def download():
    return render_template("download.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/alert")
def alert():
    return render_template("alert.html")

@main.route("/ip")
def get_ip():
    ip_content = Ip.objects(index = "0").first()
    return ip_content.ip.split("\n")[0]

@main.route("/coper_price")
@login_required
def get_coper_price():
    page = request.args.get("page",1,type = int)
    pagination = PriceInfo.objects().paginate(page=page,per_page=current_app.config["PRICE_PER_PAGE"],error_out=False)
    price_infos = pagination.items
    return render_template("price_info.html",price_infos = price_infos,pagination = pagination)

@main.route("/coper_price_jason")
@login_required
def get_coper_price_jason():
    data_list = []
    page = request.args.get("page",1,type = int)
    pagination = PriceInfo.objects().paginate(page=page,per_page=current_app.config["PRICE_PER_PAGE"],error_out=False)
    price_infos = pagination.items
    for item in price_infos:
        data_list.append(item.to_dict())
    return str(data_list)

@main.route("/table")
@login_required
def table_menu():
	try:
		user_role = current_user.role.split(",")
	except Exception as e:
		return render_template("index.html")
	if user_role[0] == "admin":
		equipments = Oderawayequipments.objects().all()
	else:
		equipments = []
		for item in user_role:
			equipments.append(Oderawayequipments.objects(SerialNum = item).first())
	return render_template("table.html",equipments = equipments)

@main.route("/config/<ser_num>",methods = ["GET","POST"])
@login_required
def config_menu(ser_num):
	role = current_user.role
	if ser_num in role or "admin" in role:
		equipment = Oderawayequipments.objects(SerialNum = ser_num).first()
	return render_template("config.html",equipment = equipment)