# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: my_values.py
# @date: 2020/05/06
import os
from utils import Constant


constant = Constant()
constant.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
constant.COVID_DB_PATH = os.path.join(
    os.path.join(constant.BASE_DIR, "database"), "covid.sqlite"
)
