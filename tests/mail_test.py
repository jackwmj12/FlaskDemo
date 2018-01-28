from flask import Flask
import os
# import ip_acquire
from flask_mail import Message,Mail

app = Flask(__name__)
mail = Mail(app)
# ...
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] ="343563813@qq.com"
app.config['MAIL_PASSWORD'] = 'biycszevokgfbhci'
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

msg = Message('test subject', sender='343563813@qq.com', recipients=['joe.lin@oderaway.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)
