import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def hello():
    return "Hello World!"