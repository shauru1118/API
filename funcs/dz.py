import json
import os
from sqlite3 import Date
from textwrap import indent
import time
from deep_translator import GoogleTranslator

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
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps({
            "dz" : False,
            "Weekday": {
                "en": translator.translate(time.strftime("%A", time.strptime(date, "%d.%m.%Y"))),
                "ru" : translator.translate(time.strftime("%A", time.strptime(date, "%d.%m.%Y")))
            },
            "Date": {
                "short": date,
                "full": translator.translate(time.strftime("%A, %d %B %Y", time.strptime(date, "%d.%m.%Y")))
            },
            "Subjects": {

            }
        }, indent=4, ensure_ascii=False))


def get_now_day_digit() -> int:
    return time.localtime().tm_wday+1

def get_now_day()-> str:
    return DAYS[get_now_day_digit()]

def get_dz(date : str):
    file_name = os.path.join(JSON_DIR, date+'.json')
    
    if os.path.exists(file_name):
        return json.load(open(file_name, 'r', encoding='utf-8'))
    else:
        make_dz_file(date)
        return json.load(open(file_name, 'r', encoding='utf-8'))
    


if __name__ == '__main__':
    print(get_dz('15.09.2025'))
    print(DAYS[time.localtime().tm_wday+1])
    print(time.localtime().tm_wday+1)