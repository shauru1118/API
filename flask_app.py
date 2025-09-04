import flask
from classes import Person
import dbfunc as db
import utils

PHIS_MATH = 1
INFO_MATH = 2

app = flask.Flask(__name__)

@app.route('/')
def index():
    return utils.list_to_str(db.get_items()).replace('\n', '<br>')

if __name__ == '__main__':
    db.Init()
    db.add_item(Person("albert", PHIS_MATH))
    app.run("0.0.0.0", port=5000, debug=False)
