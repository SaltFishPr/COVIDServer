# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: test.py
# @date: 2020/05/06
import requests

if __name__ == "__main__":
    url = "http://49.235.19.174:5000/login"
    data = {"account": "33333333", "password": "123456"}
    response = requests.post(url=url, data=data)
    print(response.text)
