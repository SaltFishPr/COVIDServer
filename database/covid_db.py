# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: covid_db.py
# @date: 2020/05/06
import sqlite3
from my_values import constant
from database.contract import ResidentEntry, RecordEntry


class AccountTable:
    @classmethod
    def create_table(cls):
        """
        创建表
        :return:
        """
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            f"CREATE TABLE {ResidentEntry.TABLE_NAME} ("
            f"{ResidentEntry.COLUMN_ID_CARD} TEXT PRIMARY KEY, "
            f"{ResidentEntry.COLUMN_PASSWORD} TEXT NOT NULL, "
            f"{ResidentEntry.COLUMN_NAME} TEXT NOT NULL, "
            f"{ResidentEntry.COLUMN_UNIT} INTEGER NOT NULL, "
            f"{ResidentEntry.COLUMN_ROOM} INTEGER NOT NULL, "
            f"{ResidentEntry.COLUMN_PHONE} INTEGER NOT NULL);"
        )
        cursor.close()
        conn.close()

    @classmethod
    def query(cls, account):
        """
        查询
        :param account: 账号，这里是身份证号
        :return: 元组数组 [()]，包含一个人的所有信息
        """
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = (
            f"SELECT * FROM {ResidentEntry.TABLE_NAME} "
            f"WHERE {ResidentEntry.COLUMN_ID_CARD}='{account}'; "
        )
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        if not res:
            return None
        return res[0]

    @classmethod
    def insert(cls, account, password):
        """
        插入
        :param account:
        :param password:
        :return:
        """
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = (
            f"INSERT INTO {ResidentEntry.TABLE_NAME} "
            f"({ResidentEntry.COLUMN_ID_CARD}, {ResidentEntry.COLUMN_PASSWORD}, "
            f"{ResidentEntry.COLUMN_NAME}, {ResidentEntry.COLUMN_UNIT}, "
            f"{ResidentEntry.COLUMN_ROOM}, {ResidentEntry.COLUMN_PHONE}) "
            f"VALUES ('{account}', '{password}', 'default', -1, -1, -1);"
        )
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    @classmethod
    def update_info(cls, account, name="default", unit=-1, room=-1, phone=-1):
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = (
            f"UPDATE {ResidentEntry.TABLE_NAME} "
            f"SET {ResidentEntry.COLUMN_NAME}='{name}', "
            f"{ResidentEntry.COLUMN_UNIT}={unit}, "
            f"{ResidentEntry.COLUMN_ROOM}={room}, "
            f"{ResidentEntry.COLUMN_PHONE}={phone} "
            f"WHERE {ResidentEntry.COLUMN_ID_CARD}='{account}' "
        )
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, account):
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = (
            f"DELETE FROM {ResidentEntry.TABLE_NAME} "
            f"WHERE {ResidentEntry.COLUMN_ID_CARD}='{account}'"
        )
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


class RecordTable:
    @classmethod
    def create_table(cls):
        """
        创建通行记录表
        :return:
        """
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            f"CREATE TABLE {RecordEntry.TABLE_NAME} "
            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            f"{RecordEntry.COLUMN_ID_CARD} TEXT NOT NULL, "
            f"{RecordEntry.COLUMN_GATE} TEXT NOT NULL, "
            f"{RecordEntry.COLUMN_TIME} INTEGER NOT NULL, "
            f"FOREIGN KEY ({RecordEntry.COLUMN_ID_CARD}) "
            f"REFERENCES {ResidentEntry.TABLE_NAME}({ResidentEntry.COLUMN_ID_CARD}) );"
        )
        cursor.close()
        conn.close()

    @classmethod
    def query(cls, account):
        """
        查询
        :param account: 账号，这里是身份证号
        :return: 元组数组 [(), (), ...]，包含一个人的所有通行信息
        """
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = (
            f"SELECT * FROM {RecordEntry.TABLE_NAME} "
            f"WHERE {RecordEntry.COLUMN_ID_CARD}='{account}'"
            f"ORDER BY {RecordEntry.COLUMN_TIME} DESC; "
        )
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res

    @classmethod
    def insert(cls, account, gate, time):
        """
        插入通行信息
        :param account:
        :param gate:
        :param time:
        :return:
        """
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = (
            f"INSERT INTO {RecordEntry.TABLE_NAME} "
            f"({RecordEntry.COLUMN_ID_CARD}, "
            f"{RecordEntry.COLUMN_GATE}, "
            f"{RecordEntry.COLUMN_TIME}) "
            f"VALUES ('{account}', '{gate}', {time});"
        )
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()
