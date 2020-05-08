# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: app.py
# @date: 2020/05/06
from flask import Flask, redirect, url_for, request, Response
from database.covid_db import AccountTable
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/login", methods=["POST"])
def login():
    account = request.form["account"]
    password = request.form["password"]
    print(f"account: {account}, password: {password}")
    res = AccountTable.query(account)
    if res == None:
        return json.dumps({"data": False, "ret_code": 2})  # 不存在此用户
    if password == res[1]:
        return json.dumps({"data": True, "ret_code": 1})  # 密码匹配
    else:
        return json.dumps({"data": False, "ret_code": 1})  # 密码不匹配


@app.route("/register", methods=["POST"])
def register():
    account = request.form["account"]
    password = request.form["password"]
    if AccountTable.query(account, password) != None:{
        return json.dumps({"data": "failure", "ret_code": 2})
    }
    AccountTable.insert(account, password)
    return json.dumps({"data": "ok", "ret_code": 1})


@app.route("/update_resident", methods=["POST"])
def update_resident_info():
    account = request.form["account"]
    name = request.form["name"]
    unit = request.form["unit"]
    room = request.form["room"]
    phone = request.form["phone"]
    AccountTable.update_info(account, name, unit, room, phone)
    return {"data": "ok", "ret_code": 1}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
