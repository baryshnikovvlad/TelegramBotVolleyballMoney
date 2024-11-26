
# Вручную бдшка
import sqlite3
from sqlite3 import Error

path = "C://Users/barys/PycharmProjects/TelegramBotVolleyballMoney/bd.sqlite3"


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)  # connection
        return connection
    except Error as e:
        print(f"The error {e} occured")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        # print(result)
        return result
    except Error as e:
        print(f"The error::  {e}   occured!")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfuly.")
    except Error as e:
        print(f"Error - {e} - was occured!")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    priority INTEGER DEFAULT 0,
    phone_number TEXT DEFAULT fuck,
    user_tg_id INTEGER
);
"""

create_visits_table = """
CREATE TABLE IF NOT EXISTS visits (
    visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_tg_id INTEGER,
    option_id INTEGER,
    poll_id INTEGER,
    date TEXT,
    price REAL
);
"""

create_users_visits_table = """
CREATE TABLE IF NOT EXISTS users_visits (
    user_tg_id INTEGER REFERENCES users,
    date TEXT REFERENCES visits,
    PRIMARY KEY (user_tg_id, date)
);
"""
