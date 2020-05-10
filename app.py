# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: app.py
# @date: 2020/05/06
import time
from flask import Flask, request
import json
from database.covid_db import AccountTable, RecordTable

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/login", methods=["POST"])
def login():
    """
    登录
    :return:
    """
    account = request.form["account"]
    password = request.form["password"]
    print(f"account: {account}, password: {password}")
    res = AccountTable.query(account)
    if res is None:
        return json.dumps({"data": False, "ret_code": 2})  # 不存在此用户
    if password == res[1]:
        return json.dumps({"data": True, "ret_code": 1})  # 密码匹配
    else:
        return json.dumps({"data": False, "ret_code": 1})  # 密码不匹配


@app.route("/register", methods=["POST"])
def register():
    """
    注册
    :return:
    """
    account = request.form["account"]
    password = request.form["password"]
    if AccountTable.query(account) is not None:
        return json.dumps({"data": "failure", "ret_code": 2})
    AccountTable.insert(account, password)
    return json.dumps({"data": "ok", "ret_code": 1})


@app.route("/post_record", methods=["POST"])
def post_record():
    """
    上传通行信息
    :return:
    """
    account = request.form["account"]
    gate = request.form["gate"]
    now_time = int(time.time())
    # 判断是否允许通过
    RecordTable.query(account)
    # ...
    RecordTable.insert(account, gate, now_time)


@app.route("/get_record/<account>")
def get_record(account):
    """
    获取通信信息
    :return:
    """
    pass


@app.route("/update_resident", methods=["POST"])
def update_resident_info():
    """
    更新用户信息
    :return:
    """
    account = request.form["account"]
    name = request.form["name"]
    unit = request.form["unit"]
    room = request.form["room"]
    phone = request.form["phone"]
    if AccountTable.query(account) is None:
        return json.dumps({"data": "failure", "ret_code": 2})
    AccountTable.update_info(account, name, unit, room, phone)
    return json.dumps({"data": "ok", "ret_code": 1})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
