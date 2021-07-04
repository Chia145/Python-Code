from flask import Flask, jsonify, request
from C136ProjectData import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "status": "success"
    }), 200

@app.route("/star")
def stars():
    name = request.args.get('Star Name')
    starData = next(i for i in data if i['Star Name'] == name)
    return jsonify({
        "data" : starData,
        "message": "Success"
    }), 200

if __name__ == "__main__":
    app.run()