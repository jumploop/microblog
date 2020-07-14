#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 19:51
# @Author  : 一叶知秋
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models,errors
