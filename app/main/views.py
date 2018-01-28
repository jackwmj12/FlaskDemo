from flask import render_template,redirect,url_for,session,request,flash,current_app
from . import main
from flask_login import login_required
from ..models import OderawayStatus,Ip,PriceInfo,User
from flask import jsonify

@main.route("/index")
@main.route("/")
def index():
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
    # page = request.args.get("page",1,type = int)
    # pagination = OderawayStatus.objects.order_by(OderawayStatus.Time,
    #                 per_page = current_app.config["FLASKY_POSTS_PER_PAGE"],
    #                 error_out =False)
    # oderstatus = pagination.items
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
