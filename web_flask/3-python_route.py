#!/usr/bin/python3
""" Python is cool"""

from flask import Flask

app = Flask(__name__)


@app.route('/',  strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<name>', strict_slashes=False)
def c(name):
    name = name.replace('_', ' ')
    return 'C {}'.format(name)


@app.route('/python/')
@app.route('/python/<text>')
def pyth_text(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == "__main__":
    """run application with port 5000 and host 0.0.0.0"""
    app.run(host='0.0.0.0', port=5000)
