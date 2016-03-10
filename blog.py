# Controller of the blog app
import sqlite3
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g

# Configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xc2\xbequ!\x86\xa1#\x87}\xf5\x94V\xaf\x03\xb7\xaa\x16U\x0b_\x05e\xf9'


app = Flask(__name__)

# Pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)


# Function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error_msg = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error_msg = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error_msg)


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/logout')
def logout():
    session.pop('logged in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
