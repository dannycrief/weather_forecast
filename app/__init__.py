from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.conf import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = Config.SECRET_KEY
db = SQLAlchemy(app)
db.create_all()
from app import routes, models
