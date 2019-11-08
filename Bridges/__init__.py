from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///test.db')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Login = LoginManager(app)

from Bridges import routes