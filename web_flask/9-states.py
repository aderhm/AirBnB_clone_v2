#!/usr/bin/python3
"""Lists all states and cities"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def get_cities_by_states():
    """Gets all states and displays them as a list in an HTML page
    """
    all_states = storage.all(State)
    return render_template('9-states.html', all_states=all_states)


@app.route("/states/<id>", strict_slashes=False)
def get_state_by_id(id):
    """Displays a state if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
