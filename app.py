#!usr/bin/env /python3
print('hello from python')
from flask import Flask, render_template
import sqlite3

if __name__ == "__main__":
    print("Ready...")

with sqlite3.connect("myhome.db") as connect:
    kursor = connect.cursor()
    kursor.execute("""CREATE TABLE IF NOT EXISTS smarthome (
        temperature REAL,
        humidity REAL,
        pressure REAL,
        latitude REAL,
        longitude REAL,
        altitude REAL,
        time REAL,
        analog1 INTEGER,
        analog2 INTEGER,
        digital1 INTEGER,
        digital2 INTEGER
        )""")
    kursor.execute("""CREATE TABLE IF NOT EXISTS relays (
            relay1 INTEGER,
            relay2 INTEGER,
            mode INTEGER
            )""")
    connect.commit()
