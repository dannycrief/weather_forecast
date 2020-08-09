import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.conf import Config

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = Config.SECRET_KEY

login_manager.init_app(app)
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
db.create_all()
from app import routes, models
