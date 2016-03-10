# Controller of the blog app
import sqlite3
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g

# Configuration
DATABASE = 'blog.db'

app = Flask(__name__)

# Pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# Function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run(debug=True)