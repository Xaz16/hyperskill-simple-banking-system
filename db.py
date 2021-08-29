import sqlite3

connection = None


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


def connect():
    global connection
    if connection is None:
        connection = sqlite3.connect('card.s3db')
        connection.row_factory = sqlite3.Row
    return connection


def read(query):
    cursor = connection.cursor()
    return cursor.execute(query).fetchall()


def write(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def disconnect():
    connection.commit()
    connection.close()
