from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
db = mongo.db

@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return online_users


@app.route('/post_data_from_sensors', methods=["POST"])
def post_data():
    sensors_details = request.get_json()
    db.sensors.insert_one(sensors_details)
    return True


if __name__ == "__main__":
    print("Ready to start app...")
    app.run(host='0.0.0.0', port=3939, debug=False)
