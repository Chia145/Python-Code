from flask import Flask, jsonify, request  

app = Flask(__name__)
contacts = [
    {
        'id': 1,
        'Name': u'Me',
        'Contact': u'1234567890', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Her',
        'Contact': u'0987654321', 
        'done': False
    }
]
@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
@app.route('/get-data')
def get_task():
    return jsonify({"data":contacts})

if __name__ == '__main__':
    app.run(debug = True)

