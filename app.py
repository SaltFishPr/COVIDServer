# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: app.py
# @date: 2020/05/06
import time
import datetime
from flask import Flask, request
import json
from my_values import constant
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
        return json.dumps({"data": False, "ret_code": constant.DB_FAILURE})  # 不存在此用户
    if password == res[1]:
        return json.dumps({"data": True, "ret_code": constant.SUCCESS})  # 密码匹配
    else:
        return json.dumps({"data": False, "ret_code": constant.SUCCESS})  # 密码不匹配


@app.route("/register", methods=["POST"])
def register():
    """
    注册
    :return:
    """
    account = request.form["account"]
    password = request.form["password"]
    if AccountTable.query(account) is not None:
        return json.dumps({"data": "failure", "ret_code": constant.DB_FAILURE})
    AccountTable.insert(account, password)
    return json.dumps({"data": "ok", "ret_code": constant.SUCCESS})


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
    res = RecordTable.query(account)
    date1 = datetime.datetime.fromtimestamp(res[0][2])
    date2 = datetime.datetime.fromtimestamp(time.time())
    if date1.date() == date2.date():
        return json.dumps({"result": "forbid", "ret_code": constant.DB_FAILURE})
    else:
        RecordTable.insert(account, gate, now_time)
        return json.dumps({"result": "permit", "ret_code": constant.SUCCESS})


@app.route("/get_record/<account>")
def get_record(account):
    """
    获取通信信息
    :return:
    """
    if not RecordTable.query(account):
        return json.dumps({"data": None, "ret_code": constant.DB_FAILURE})
    res = []
    for i in RecordTable.query(account):
        temp = {"gate": i[2], "time": str(datetime.datetime.fromtimestamp(i[3]).date())}
        res.append(temp)
    print(res)
    return json.dumps({"data": res, "ret_code": constant.SUCCESS})


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
        return json.dumps({"data": "failure", "ret_code": constant.DB_FAILURE})
    AccountTable.update_info(account, name, unit, room, phone)
    return json.dumps({"data": "ok", "ret_code": constant.SUCCESS})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
