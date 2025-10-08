# import requests
# from pprint import pprint

# data = {
#     "date": "03.10.2025", 
#     "sj":"Алгебра", 
#     "hw":"6.7, 6.9, 6.13"
# }


# res = requests.post('http://localhost:5000/api/add-dz', json=data)

# pprint(res.json(), indent=4, depth=4)



homeworks = {'Химия': 'Выучить углеводороды. Будет самостоятельная.', 'Русский язык': '§11, упр 73, 78, и выучить материал на странице 51', 'Русский': '§11, упр 73, 78, и выучить материал на странице 51'}
print(homeworks.get("Русский язык"))
