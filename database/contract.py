# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: contract.py
# @date: 2020/05/06


class ResidentEntry:
    TABLE_NAME = "residents"
    COLUMN_ID_CARD = "id_card"
    COLUMN_PASSWORD = "password"
    COLUMN_NAME = "nickname"
    COLUMN_UNIT = "unit"
    COLUMN_ROOM = "room"
    COLUMN_PHONE = "phone"


class RecordEntry:
    TABLE_NAME = "records"
    COLUMN_ID_CARD = "id_card"
    COLUMN_TIME = "time"
    COLUMN_GATE = "gate"
