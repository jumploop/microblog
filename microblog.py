#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 19:56
# @Author  : 一叶知秋
# @File    : microblog.py
# @Software: PyCharm
from app import create_app, db,cli
from app.models import User, Post

app=create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
