# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: covid_db.py
# @date: 2020/05/06
import sqlite3
from my_values import constant
from database.contract import ResidentEntry


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
        sql = f"SELECT * FROM {ResidentEntry.TABLE_NAME} WHERE {ResidentEntry.COLUMN_ID_CARD}='{account}';"
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
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
        sql = f"INSERT INTO {ResidentEntry.TABLE_NAME} ({ResidentEntry.COLUMN_ID_CARD}, {ResidentEntry.COLUMN_PASSWORD}, {ResidentEntry.COLUMN_NAME}, {ResidentEntry.COLUMN_UNIT}, {ResidentEntry.COLUMN_ROOM}, {ResidentEntry.COLUMN_PHONE}) VALUES ('{account}', '{password}', 'default', -1, -1, -1);"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    @classmethod
    def update_info(cls, account, name="default", unit=-1, room=-1, phone=-1):
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = f"UPDATE {ResidentEntry.TABLE_NAME} SET {ResidentEntry.COLUMN_NAME}='{name}', {ResidentEntry.COLUMN_UNIT}={unit}, {ResidentEntry.COLUMN_ROOM}={room}, {ResidentEntry.COLUMN_PHONE}={phone} WHERE {ResidentEntry.COLUMN_ID_CARD}='{account}'"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, account):
        conn = sqlite3.connect(constant.COVID_DB_PATH)
        cursor = conn.cursor()
        sql = f"DELETE FROM {ResidentEntry.TABLE_NAME} WHERE {ResidentEntry.COLUMN_ID_CARD}='{account}'"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    # AccountTable.create_table()
    # AccountTable.insert("33333333", "123456")
    # AccountTable.update_info(account="33333333", name="saltfish")
    # print(AccountTable.query("33333333"))
    pass
