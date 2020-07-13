#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 19:51
# @Author  : 一叶知秋
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask
from config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
from app import routes
