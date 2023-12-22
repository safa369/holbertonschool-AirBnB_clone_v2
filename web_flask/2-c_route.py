#!/usr/bin/python3
""" Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/',  strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(name):
    name = name.replace('_', ' ')
    return 'C {}'.format(name)


if __name__ == "__main__":
    """run application with port 5000 and host 0.0.0.0"""
    app.run(host='0.0.0.0', port=5000)
