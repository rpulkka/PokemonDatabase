from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application import models

db.create_all()

