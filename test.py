# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: test.py
# @date: 2020/05/06
import time
import datetime
import json
import app
from database.covid_db import AccountTable, RecordTable

if __name__ == "__main__":
    # AccountTable.create_table()
    # AccountTable.insert("33333333", "123456")
    # RecordTable.create_table()
    # RecordTable.insert("33333333", 1, time.time())
    # RecordTable.insert("33333333", 3, time.time())
    # RecordTable.insert("33333333", 2, time.time())

    # print(datetime.datetime.fromtimestamp(time.time()).date())
    # url = "http://127.0.0.1:5000/get_record/33333333"
    # response = requests.get(url)
    # print(response.text)
    # print(RecordTable.query("33333333"))
    print(app.get_record("33333333"))
    # print(json.dumps(RecordTable.query("33333333")))
