import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import basedir


# Initialize Flask app
app = Flask(__name__)

app.config.from_object('config') 

# Variable represents sqlalchemy
db = SQLAlchemy(app)

mail = Mail(app)

from app import views