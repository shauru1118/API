from flask import Flask, jsonify, request 
from classes import Person
import dbfunc as db
import utils

app = Flask(__name__)

@app.route('/')
def index():
    return utils.dict_to_str(db.get_items()).replace('\n', '<br>')

# do add to db from json
@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    id = data['id']
    name = data['name']
    prof = db.PHIS_MATH if data['prof'] == 'phis' else db.INFO_MATH
    db.add_item(id, name, prof)
    return jsonify(db.get_items())

# get JSON with users
@app.route('/get')
def get_user():
    res = db.get_items()
    if res is None or len(res) == 0:
        return jsonify({}), 404
    return jsonify(res)

@app.route('/delete', methods=['POST'])
def delete_user():
    data = request.get_json()
    id = data['id']
    db.delete_item(id)
    return jsonify(db.get_items())

@app.route('/phis')
def get_phis():
    return jsonify(db.get_phis())

@app.route('/info')
def get_info():
    return jsonify(db.get_info())


if __name__ == '__main__':
    db.Init()
    app.run("0.0.0.0", port=5000, debug=False)
