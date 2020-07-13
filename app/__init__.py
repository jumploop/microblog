#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 19:51
# @Author  : 一叶知秋
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)

from app import routes
