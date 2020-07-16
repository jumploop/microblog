#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 0:54
# @Author  : 一叶知秋
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main import routes
