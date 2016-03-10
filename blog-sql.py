# Database for blog app
import sqlite3

with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()
    # Create table posts
    c.execute("""CREATE TABLE posts
    (title TEXT, post TEXT)""")
    # Insert content
    c.execute('INSERT INTO posts VALUES("My first blog", "Hello world! This is my first app with Flask and a \
        starting point to explore the world.")')