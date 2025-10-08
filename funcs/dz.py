import json
import os
import funcs.dbfunc as db
import time
from deep_translator import GoogleTranslator
from pprint import pprint

JSON_DIR = 'jsons'
if not os.path.exists(JSON_DIR):
    os.mkdir(JSON_DIR)

DAYS = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}

translator = GoogleTranslator(source='auto', target='ru')

def make_dz_file(date : str):
    file_name = os.path.join(JSON_DIR, date+'.json')
    day = time.strftime("%A", time.strptime(date, "%d.%m.%Y"))
    data = json.load(open(os.path.join(JSON_DIR, f'{day.lower()}.json'), 'r', encoding='utf-8'))
    data["Date"]["short"] = date
    data["Date"]["full"] = translator.translate(time.strftime("%A, %d %B %Y", time.strptime(date, "%d.%m.%Y")))

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
    
    return data


def get_now_day_digit() -> int:
    return time.localtime().tm_wday+1

def get_now_day()-> str:
    return DAYS[get_now_day_digit()]

def get_dz(day: int, date : str, id):
    # file_name = os.path.join(JSON_DIR, date+'.json')
    
    # if os.path.exists(file_name):
    #     return json.load(open(file_name, 'r', encoding='utf-8'))
    # else:
    #     return make_dz_file(date)
    
    user_prof = None
    user_index = None
    if id:
        user_prof = db.get_prof(int(id))
        if user_prof == 1:
            user_index = 0
        elif user_prof == 0:
            user_index = 1
        
    
    file_name = os.path.join(JSON_DIR, DAYS[day]+'.json')
    data: dict = json.load(open(file_name, 'r', encoding='utf-8'))
    
    data["Date"]["short"] = date
    data["Date"]["full"] = translator.translate(time.strftime("%A, %d %B %Y", time.strptime(date, "%d.%m.%Y")))
    homeworks = db.get_homework(date)
    homeworks = {k.strip().lower().replace('\xa0', ' '): v for k, v in homeworks.items()}
    to_del = []
    # if len(homeworks) == 0:
    #     return data
    print("!!!!!!!!! _______________", f"{date = }", f"{day = }", f"{id = }", f"{user_prof = }", 
                                       f"{homeworks = }", f"{list(homeworks.keys()) = }", sep="\n")
    for subject, subject_data in data["Subjects"].items():
        sj: str = subject_data.get('sj').strip()
        if "/" in sj:
            print(f"/ in {sj = }")
            sj = sj.split("/")[user_index].strip()
            subject_data["room"] = subject_data["room"].split("/")[user_index].strip()
        if sj == "Домой":
            print(f"Домой = {sj=}")
            to_del.append(subject)
            continue
        homework = homeworks.get(sj.strip().lower().replace('\xa0', ' '), 'нет дз')
        # print("!!!!!!!!! _______________", sj, sep="\n")
        # if "/" in homework:
        #     if user_index in [0, 1]:
        #         sj = sj.split('/')
        #         subject_data['sj'] = sj[user_index].strip()
        #         subject_data['hw'] = homework.split("/")[user_index]
        #         subject_data['room'] = subject_data['room'].split("/")[user_index].strip()
        #     else:
        #         subject_data['hw'] = homework
                
        # else:
        subject_data['hw'] = homework
        subject_data['sj'] = sj
        print(f"{sj in homeworks.keys() = }", f"'{repr(sj)}'", f"'{repr(homework)}'", "-"*40, sep="\n")

    for i in to_del:
        data["Subjects"].pop(i)
    data["Count"] -= len(to_del)

    return data

def add_homework(date:str, sj:str, hw:str):
    db.add_homework(date, sj, hw)
    

if __name__ == '__main__':
    date = '16.09.2025'
    day = time.strftime("%A", time.strptime(date, "%d.%m.%Y"))
    data = json.load(open(os.path.join(JSON_DIR, f'{day.lower()}.json'), 'r', encoding='utf-8'))
    print(date)
    print(day)
    pprint(data, indent=4, depth=4)
    
