from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

@app.route('/') # this is simple get request
def test_page():
    body = requests.get("https://api.kontur.ru/market/v1/shops", headers={"x-kontur-apikey": "real api key"})
    return body.content

@app.route('/test')
def hello_page():
    return 'Hello, page from flask!'

if __name__ == "__main__":
    print("Ready to start app...")
    app.run(host='0.0.0.0', port=80, debug=False)