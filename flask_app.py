from flask import Flask, jsonify, request 
from classes import Person
import dbfunc as db
import utils

PHIS_MATH = "phis"
INFO_MATH = "inf"

app = Flask(__name__)

@app.route('/')
def index():
    return utils.dict_to_str(db.get_items()).replace('\n', '<br>')

# do add to db from json
@app.route('/add', methods=['POST'])
def add_user():
    data = request.args
    name = data['name']
    prof = data['prof']
    db.add_item(Person(name, prof))
    return jsonify(db.get_items())

# get JSON with users
@app.route('/get')
def get_user():
    return jsonify(db.get_items())


if __name__ == '__main__':
    db.Init()
    # db.add_item(Person("albert", PHIS_MATH))
    # db.add_item(Person("ivan", PHIS_MATH))
    # db.add_item(Person("danya", INFO_MATH))
    app.run("0.0.0.0", port=5000, debug=False)
