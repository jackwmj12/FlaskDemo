from init import create_app,Manager,Migrate,db,MigrateCommand
from flask_mail import Mail,Message
from flask import render_template

app = create_app("default")
mail = Mail(app)
manager = Manager(app)
# migrate = Migrate(app,db)
# manager.add_command("db",MigrateCommand)

def send_mail(to,subject,template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

if __name__=='__main__':
    manager.run()