#!/usr/bin/python3
""" Python is cool"""

from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth_text(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """return a page HTML"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        test = True
    else:
        test = False
    return render_template('6-number_odd_or_even.html', n=n, test=test)


if __name__ == "__main__":
    """run application with port 5000 and host 0.0.0.0"""
    app.run(host='0.0.0.0', port=5000)
