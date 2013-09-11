# Email Function

from flask.ext.mail import Message
from app import mail
from config import ADMINS, MAIL_USERNAME
def send_email(name, sender_email, text_body):
    msg = Message('W&W Contact Form', sender = (name, sender_email), recipients = ADMINS)
    msg.body = text_body
    mail.send(msg)
