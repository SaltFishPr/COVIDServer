# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: test.py
# @date: 2020/05/06
import time
import datetime
import json
import requests
from database.covid_db import AccountTable, RecordTable

if __name__ == "__main__":
    # RecordTable.create_table()
    # RecordTable.insert("33333333", 1, time.time())
    # print(datetime.datetime.fromtimestamp(time.time()).date())
    url = "http://127.0.0.1:5000/get_record/33333333"
    response = requests.get(url)
    print(response.text)
    # print(RecordTable.query("33333333"))
    # print(json.dumps(RecordTable.query("33333333")))
