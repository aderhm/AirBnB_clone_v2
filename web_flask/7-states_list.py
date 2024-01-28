#!/usr/bin/python3
"""Lists all states"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_list_of_states():
    from models.state import State
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def close_session():
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
