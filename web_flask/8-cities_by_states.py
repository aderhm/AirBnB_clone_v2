#!/usr/bin/python3
"""Lists all states and cities"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_list_of_states():
    """Gets all states and cities,
    and displays cities by states in an HTML page
    """
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
