import time
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import funcs.dbfunc as db
import funcs.utils as utils
import funcs.dz as dz

app = Flask(__name__)
CORS(app)
db.Init()

@app.route('/')
def index():
    return render_template('index.html')

# ! database api

# * do add to db from json
@app.route('/api/add-user', methods=['POST'])
def add_user():
    data = request.get_json()
    id = data['id']
    prof = data['prof']
    db.add_user(id, prof)
    return jsonify(db.get_users())

@app.route('/api/add-user-args')
def add_user_args():
    id = request.args.get('id')
    prof = request.args.get('prof')
    db.add_user(id, prof)
    return jsonify(db.get_users())

# get JSON with users
@app.route('/api/get-users')
def get_users():
    res = db.get_users()
    if res is None or len(res) == 0:
        return jsonify({"error" : "no users"})
    return jsonify(res)

@app.route('/api/delete-user', methods=['POST'])
def delete_user():
    data = request.get_json()
    id = data['id']
    db.delete_item(id)
    return jsonify(db.get_users())

@app.route('/api/get-users-phis')
def get_phis():
    return jsonify(db.get_phis())

@app.route('/api/get-users-info')
def get_info():
    return jsonify(db.get_info())

# ! dz api

@app.route('/api/get-dz', methods=['POST'])
def get_dz():
    day = request.json.get('day', dz.get_now_day_digit())
    now_day = dz.get_now_day_digit()
    if now_day > day:
        date = time.strftime("%d.%m.%Y", time.localtime(time.time() + 86400 * (7 - (now_day - day))))
        return jsonify(dz.get_dz(date))
    elif now_day <= day:
        date = time.strftime("%d.%m.%Y", time.localtime(time.time() + 86400 * (day - now_day)))
        return jsonify(dz.get_dz(date))


if __name__ == '__main__':
    app.run("0.0.0.0", port=8000, debug=True)

