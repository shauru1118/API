from flask import Flask, jsonify, request, render_template
import dbfunc as db
import utils

app = Flask(__name__)
db.Init()

@app.route('/')
def index():
    return render_template('index.html')

# do add to db from json
@app.route('/api/add-user', methods=['POST'])
def add_user():
    data = request.get_json()
    id = data['id']
    prof = data['prof']
    db.add_user(id, prof)
    return jsonify(db.get_users())

# get JSON with users
@app.route('/api/get-users')
def get_users():
    res = db.get_users()
    if res is None or len(res) == 0:
        return jsonify({"error" : "no users"}), 404
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


if __name__ == '__main__':
    app.run("0.0.0.0", port=8000, debug=True)

