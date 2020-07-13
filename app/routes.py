#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 19:54
# @Author  : 一叶知秋
# @File    : routes.py
# @Software: PyCharm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
