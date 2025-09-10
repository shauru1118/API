import sqlite3

DATABASE_FILE = 'main.db'
USERS_TABLE = 'users'
PROFILS_TABLE = 'profs'
INFO_MATH = 0
PHIS_MATH = 1

def Init():
    # create tables
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {USERS_TABLE} (id INTEGER PRIMARY KEY, prof INTEGER)")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {PROFILS_TABLE} (profile INTEGER, description TEXT)")
    con.commit()

    # check for profiles
    cur.execute(f"SELECT * FROM {PROFILS_TABLE} WHERE profile = ?", (PHIS_MATH,))
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO {PROFILS_TABLE} (profile, description) VALUES (?, ?)", (INFO_MATH, "информатико-математический"))
        cur.execute(f"INSERT INTO {PROFILS_TABLE} (profile, description) VALUES (?, ?)", (PHIS_MATH, "физико-математический"))
        con.commit()

    con.close()

def add_user(id, prof):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"INSERT INTO {USERS_TABLE} (id, prof) VALUES (?, ?)", (id, prof))
    con.commit()
    con.close()
    return

def delete_user(id):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"DELETE FROM {USERS_TABLE} WHERE id = ?", (id,))
    con.commit()
    con.close()
    return

def get_users():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE}")
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[int(user[0])] = (user[1], str(user[2]))
    return data

def get_phis():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE prof = ?", (PHIS_MATH,))
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[int(user[0])] = (user[1], str(user[2]))
    return data

def get_info():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE prof = ?", (INFO_MATH,))
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[int(user[0])] = (user[1], str(user[2]))
    return data


