import sqlite3
from pprint import pprint


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

def get_homework(date: str) -> dict:
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT subject, hw FROM {HOME_WORKS_TABLE} WHERE date = ?", (date,))
    hws = cur.fetchall()
    con.close()
    return {sj[0]: sj[1] for sj in hws}

def get_all_homeworks() -> list:
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"SELECT date, subject, hw FROM {HOME_WORKS_TABLE}")
    hws = cur.fetchall()
    con.close()
    return hws

def add_homework(date: str, subject: str, hw: str):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"REPLACE INTO {HOME_WORKS_TABLE} (date, subject, hw) " + 
                "VALUES (?, ?, ?) ",
                (date, subject, hw))
    con.commit()
    con.close()
    return

def delete_subject_homework(date: str, subject: str):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"DELETE FROM {HOME_WORKS_TABLE} WHERE date = ? AND subject = ?", (date, subject))
    con.commit()
    con.close()
    return

def delete_homework(date: str):
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute(f"DELETE FROM {HOME_WORKS_TABLE} WHERE date = ?", (date,))
    con.commit()
    con.close()
    return    pprint(get_all_homeworks(), indent=4)



if __name__ == '__main__':
    Init()
    pprint(get_all_homeworks(), indent=4, depth=2, width=100)
    # print("\n\n")
    # date_ = '03.10.2025'
    # delete_homework(date_)
    # add_homework(date_, 'Литература', 'Будет русский (дз с паронимами)')
    # add_homework(date_, 'Английский язык', 'WB: p. 14 ex. 1-3')
    # add_homework(date_, 'Алгебра', '6.7, 6.9, 6.13')
    # add_homework(date_, 'История', '6 параграф, <<почему 1920-ые — "ревущие двадцатые">>')
    # add_homework(date_, 'Информатика', 'Презентации')
    # add_homework(date_, 'Физика', 'Нужны информаторы для инфмат')
    
    # # add_homework(date_, 'Домой / Физика', 'Домой / Нужны информаторы для инфмат группы')

    # pprint(get_all_homeworks(), indent=4, depth=2, width=100)

