from flask_mail import Message
from flask import render_template
from . import mail
from flask import current_app
from threading import Thread

#to 接收方
#sender 发送方
#subject 主题
#template 内容
def send_async_mail(to,subject,template,**kwargs):#发送邮件
    msg = Message(current_app.config["FLASKY_MAIL_SUBJECT_PREFIX"] + subject,sender = current_app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

def send_async_email(app,msg):
    with app.app_context():
        for i in range(0,5):
            try:
                mail.send(msg)
                return True
            except Exception as e:
                i =+ 1
                print("***********\nerr is {} .index is {}\n**********".format(e,i))
    return False
#发送异步邮件
def send_email(to,subject,template,**kwargs):#发送邮件
    msg = Message(current_app.config["FLASKY_MAIL_SUBJECT_PREFIX"] + subject,sender = current_app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email,args= [app,msg])
    thr.start()
    return thr