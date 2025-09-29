from ast import List
import sqlite3

DATABASE_FILE = 'main.db'
USERS_TABLE = 'users'
PROFILS_TABLE = 'profs'
HOME_WORKS_TABLE = 'homeworks'
INFO_MATH = 0
PHIS_MATH = 1

def Init():
    # create tables
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {USERS_TABLE} (id INTEGER PRIMARY KEY, prof INTEGER)")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {PROFILS_TABLE} (profile INTEGER, description TEXT)")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {HOME_WORKS_TABLE} (date TEXT, subject TEXT, hw TEXT)")
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
    cur.execute(f"REPLACE INTO {USERS_TABLE} (id, prof) VALUES (?, ?)", (int(id), int(prof)))    
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
        data[user[0]] = user[1]
    return data

def get_phis():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE prof = ?", (PHIS_MATH,))
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[user[0]] = user[1]
    return data

def get_info():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE prof = ?", (INFO_MATH,))
    users = cur.fetchall()
    con.close()
    data = {}
    for user in users:
        data[user[0]] = user[1]
    return data

def get_prof(id: int) -> int:
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {USERS_TABLE} WHERE id = ?", (id,))
    user = cur.fetchone()
    con.close()
    return user[1]

def get_homework(date: str) -> list:
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT subject, hw FROM {HOME_WORKS_TABLE} WHERE date = ?", (date,))
    hws = cur.fetchall()
    con.close()
    return {sj[0]: sj[1] for sj in hws}

def get_all_homeworks() -> list:
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {HOME_WORKS_TABLE}")
    hws = cur.fetchall()
    con.close()
    return hws

def add_homework(date: str, subject: str, hw: str):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"REPLACE INTO {HOME_WORKS_TABLE} (date, subject, hw) VALUES (?, ?, ?)", (date, subject, hw))
    con.commit()
    con.close()
    return

if __name__ == '__main__':
    Init()
    add_homework('30.09.2025', 'Алгебра', 'производная')
    print(get_all_homeworks())