# Controller of the blog app
import sqlite3
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from functools import wraps

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


# Define login_required decorators
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        flash('You need to log in first.')
        return redirect(url_for('login'))
    return wrap


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


@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required, please try again.")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('INSERT INTO posts (title, post) VALUES(?, ?)', [request.form['title'], request.form['post']])
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted.')
        return redirect(url_for('main'))


@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('SELECT * FROM posts')
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html', posts=posts)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
