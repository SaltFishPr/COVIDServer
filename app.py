# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: app.py
# @date: 2020/05/06
from flask import Flask, redirect, url_for, request
from database.covid_db import AccountTable
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]
        res = AccountTable.query(account)
        if password == res[1]:
            return json.dumps({"data": True, "ret_code": 1})
        else:
            return json.dumps({"data": False, "ret_code": 1})
    else:
        return json.dumps({"data": None, "ret_code": 2})


@app.route("/insert_resident", methods=["GET", "POST"])
def insert_resident():
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]
        AccountTable.insert(account, password)
        return {"data": "ok", "ret_code": 1}
    else:
        return {"data": None, "ret_code": 2}


@app.route("/update_resident", methods=["GET", "POST"])
def update_resident_info():
    if request.method == "POST":
        account = request.form["account"]
        name = request.form["name"]
        unit = request.form["unit"]
        room = request.form["room"]
        phone = request.form["phone"]
        AccountTable.update_info(account, name, unit, room, phone)
        return {"data": "ok", "ret_code": 1}
    else:
        return {"data": None, "ret_code": 2}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
