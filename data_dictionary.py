#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version 3.7.1

import mysql.connector
import importlib
import sys


def generate(database_name):
    """
    生成数据库字典表
    """
    importlib.reload(sys)

    conn = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        user='root',
        password='123456',
        database='information_schema',
        use_pure=True
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT table_name, table_comment FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_schema='%s'" % database_name
    )

    tables = cursor.fetchall()

    markdown_table_header = """\n\n\n### %s (%s) \n| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |\n| :--: |----| ---- | ---- | ---- |\n"""
    markdown_table_row = """| %s | %s | %s | %s | %s |"""

    f = open(database_name + '.md', 'w')

    for table in tables:

        cursor.execute(
            "SELECT ordinal_position, column_name, column_type, is_nullable, column_comment "
            "FROM information_schema.columns WHERE table_schema='%s' AND table_name='%s'" % (
                database_name, table[0]
            )
        )

        tmp_table = cursor.fetchall()
        p = markdown_table_header % (table[0], remove_newline(table[1]))
        for col in tmp_table:
            p += (remove_newline(markdown_table_row % col) + "\n")
        print(p)
        f.writelines(p)

    f.close()


def remove_newline(text):
    """
    去除文本中的换行符号
    """
    return text.replace("\r", "").replace("\n", "")


if __name__ == '__main__':
    generate('输入要生成的数据库名')
