#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 19:54
# @Author  : 一叶知秋
# @File    : routes.py
# @Software: PyCharm
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    # return 'Hello, World!'
    user = {'username': 'miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
