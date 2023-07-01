from flask.ext.mail import Message
from app import CREDENCIAIS

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients = [to],
        html = template,
        sender = 
    )
    mail.send(msg)
    