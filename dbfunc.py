import sqlite3
from classes import Person

DATABASE_FILE = 'main.db'
USERS_TABLE = 'users'

def Init():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {USERS_TABLE} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, prof TEXT)")
    con.commit()    
    con.close()

def add_item(person : Person):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"INSERT INTO {USERS_TABLE} (name, prof) VALUES (?, ?)", (person.name, person.prof))
    con.commit()
    con.close()

def get_items():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE}")
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[int(user[0])] = user[1] + " - " + str(user[2])
    return data
