#!usr/bin/env /python3
from flask import Flask, jsonify, request
import sqlite3

if __name__ == "__main__":
    print("Ready...")

with sqlite3.connect("myhome.db") as connect:
    kursor = connect.cursor()
    kursor.execute("""CREATE TABLE IF NOT EXISTS iot_sensors (
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
    kursor.execute("""CREATE TABLE IF NOT EXISTS iot_relays (
            relay1 INTEGER,
            relay2 INTEGER,
            power_mode INTEGER,
            transfer_mode INTEGER
            )""")
    connect.commit()
    kursor.execute("SELECT relay1 FROM iot_relays")
    if kursor.fetchone() is None:
        kursor.execute(f"INSERT INTO iot_relays VALUES ({0},{0},{0},{0})")
    else:
        pass
    connect.commit()

app = Flask(__name__)

@app.route('/')
def rootlink():
    return "this is root"

@app.route('/relays_data', methods=["GET"])
def get_relays():
    with sqlite3.connect("myhome.db") as connect:
        kursor = connect.cursor()
    for relays in kursor.execute("SELECT * FROM iot_relays"):
        relays_data = {
            "relay1": bool(relays[0]),
            "relay2": bool(relays[1]),
            "power_mode": bool(relays[2]),
            "transfer_mode": bool(relays[3])
        }
        print(relays_data)
    return jsonify(relays_data)

@app.route('/change_relays_data', methods=["POST"])
def post_relays():
    relays_details = request.get_json()
    relay1 = relays_details["relay1"]
    relay2 = relays_details["relay2"]
    power_mode = relays_details["power_mode"]
    transfer_mode = relays_details["transfer_mode"]

    with sqlite3.connect("myhome.db") as connect:
        kursor = connect.cursor()

    kursor.execute(f"UPDATE iot_relays SET relay1 = {relay1}")
    kursor.execute(f"UPDATE iot_relays SET relay2 = {relay2}")
    kursor.execute(f"UPDATE iot_relays SET power_mode = {power_mode}")
    kursor.execute(f"UPDATE iot_relays SET transfer_mode = {transfer_mode}")
    connect.commit()
    return True

@app.route('/post_data_from_sensors', methods=["POST"])
def post_data():
    sensors_details = request.get_json()
    temperature = sensors_details["temperature"]
    humidity = sensors_details["humidity"]
    pressure = sensors_details["pressure"]
    latitude = sensors_details["latitude"]
    longitude = sensors_details["longitude"]
    altitude = sensors_details["altitude"]
    time = sensors_details["time"]
    analog1 = sensors_details["analog1"]
    analog2 = sensors_details["analog2"]
    digital1 = sensors_details["digital1"]
    digital2 = sensors_details["digital2"]
    statement = "INSERT INTO iot_sensors(temperature, humidity, pressure, latitude, longitude, altitude, time, analog1, analog2, digital1, digital2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    with sqlite3.connect("myhome.db") as connect:
        kursor = connect.cursor()
    kursor.execute(statement, [temperature, humidity, pressure, latitude, longitude, altitude, time, analog1, analog2, digital1, digital2])
    connect.commit()
    return True


if __name__ == "__main__":
    print("Ready to start app...")
    app.run(host='0.0.0.0', port=3932, debug=False)