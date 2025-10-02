import requests
from pprint import pprint

data = {
    "date": "03.10.2025", 
    "sj":"Алгебра", 
    "hw":"6.7, 6.9, 6.13"
}


res = requests.post('http://localhost:5000/api/add-dz', json=data)

pprint(res.json(), indent=4, depth=4)

