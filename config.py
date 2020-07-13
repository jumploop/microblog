#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 21:02
# @Author  : 一叶知秋
# @File    : config.py
# @Software: PyCharm
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
