#all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    filename = os.path.join(app.instance_path, 'application.cfg')
    return filename

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/index')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        return render_template('hello.html')
    else:
        return render_template('login.html', error=error)

with app.test_request_context('/login', method='POST'):
    print login()
    print url_for('hello_world')
    print url_for('hello')
    print url_for('hello', next='/')
    print url_for('show_user_profile', username='Wenhua')
    print url_for('static', filename='style.css')


if __name__ == '__main__':
    app.run(debug=True)