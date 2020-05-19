# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: test.py
# @date: 2020/05/06
import time
import datetime
import json
import requests
import app
from database.covid_db import AccountTable, RecordTable

if __name__ == "__main__":
    url = "http://49.235.19.174:5000/post_record"
    data = {"account": "11111122222222aabb", "gate": "north"}
    response = requests.post(url, data)
    print(response.text)
