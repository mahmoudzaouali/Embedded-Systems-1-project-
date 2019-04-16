import sqlite3

with sqlite3.connect("RegistrationDatabase") as conn:
    c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user(
              userID INTEGER PRIMARY KEY,
              username VARCHAR(20) NOT NULL,
              first_name VARCHAR(20) NOT NULL,
              surname  VARCHAR(20) NOT NULL,
              password VARCHAR(20) NOT NULL
              )''')