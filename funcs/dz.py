import json
import os
import time

JSON_DIR = 'jsons'

DAYS = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}

def get_now_day_digit() -> int:
    return time.localtime().tm_wday+1

def get_now_day()-> str:
    return DAYS[get_now_day_digit()]

def get_dz(date : str):
    file_name = os.path.join(JSON_DIR, date+'.json')
    
    if os.path.exists(file_name):
        return json.load(open(file_name, 'r', encoding='utf-8'))
    
    return {"error": "no dz"}


if __name__ == '__main__':
    print(get_dz('15.09.2025'))
    print(DAYS[time.localtime().tm_wday+1])
    print(time.localtime().tm_wday+1)