import sqlite3
from classes import Person

DATABASE_FILE = 'main.db'
USERS_TABLE = 'users'
PHIS_MATH = "phis"
INFO_MATH = "inf"

def Init():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {USERS_TABLE} (id INTEGER PRIMARY KEY, name TEXT, prof TEXT)")
    con.commit()
    con.close()

def add_item(id, name, prof):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"INSERT INTO {USERS_TABLE} (id, name, prof) VALUES (?, ?, ?)", (id, name, prof))
    con.commit()
    con.close()
    return

def delete_item(id):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"DELETE FROM {USERS_TABLE} WHERE id = ?", (id,))
    con.commit()
    con.close()
    return

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

def get_phis():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE prof = ?", (PHIS_MATH,))
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[int(user[0])] = user[1] + " - " + str(user[2])
    return data

def get_info():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE prof = ?", (INFO_MATH,))
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[int(user[0])] = user[1] + " - " + str(user[2])
    return data