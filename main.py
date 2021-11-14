from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db':'IOTdatabase',
    'host':'localhost',
    'port':'27017'
}

db = MongoEngine(app)

class Sensors(db.Document):
    hadrware = db.StringField(required=True)
    temperature = db.FloatField()
    humidity = db.FloatField()
    pressure = db.FloatField()
    latitude = db.FloatField()
    longitude = db.FloatField()
    altitude = db.FloatField()
    time = db.FloatField()
    analog1 = db.FloatField()
    analog2 = db.FloatField()
    digital1 = db.IntField()
    digital2 = db.IntField()

class Relays(db.Document):
    hadrware = db.StringField(required=True)
    relay1 = db.IntField()
    relay2 = db.IntField()
    power_mode = db.IntField()
    transfer_mode = db.IntField()

@app.route('/get_sensors/<id>')
def  get_sensors(hard_id: str):
    sensors = Sensors.objects.first_or_404(hardware=hard_id)
    return  jsonify(sensors), 200

@app.route('/get_relays/<id>')
def  get_relays(hard_id: str):
    relays = Relays.objects.first_or_404(hardware=hard_id)
    return  jsonify(relays), 200

@app.route('/set_relays/', methods=["PUT"])
def update_relays(id):
    body = request.get_json()
    relays = Relays.objects.get_or_404(hadrware=id)
    relays.update(**body)
    return True

@app.route('/set_sensors/<id>', methods=['PUT'])
def update_sensors(id):
    body = request.get_json()
    sensors = Sensors.objects.get_or_404(hadrware=id)
    sensors.update(**body)
    return True

if __name__ == "__main__":
    print("Ready to start app...")
    app.run(host='0.0.0.0', port=8088, debug=False)
