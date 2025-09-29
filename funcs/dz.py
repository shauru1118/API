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

def get_dz(day: int, date : str):
    # file_name = os.path.join(JSON_DIR, date+'.json')
    
    # if os.path.exists(file_name):
    #     return json.load(open(file_name, 'r', encoding='utf-8'))
    # else:
    #     return make_dz_file(date)
    
    file_name = os.path.join(JSON_DIR, DAYS[day]+'.json')
    data = json.load(open(file_name, 'r', encoding='utf-8'))
    
    data["Date"]["short"] = date
    data["Date"]["full"] = translator.translate(time.strftime("%A, %d %B %Y", time.strptime(date, "%d.%m.%Y")))
    homeworks = db.get_homework(date)
    for subject, subject_data in data["Subjects"].items():
        sj = subject_data.get('sj')
        subject_data['hw'] = homeworks.get(sj, '')

    return data
    

if __name__ == '__main__':
    date = '16.09.2025'
    day = time.strftime("%A", time.strptime(date, "%d.%m.%Y"))
    data = json.load(open(os.path.join(JSON_DIR, f'{day.lower()}.json'), 'r', encoding='utf-8'))
    print(date)
    print(day)
    pprint(data, indent=4, depth=4)
    
