import json
import requests
from pprint import pprint


res = requests.post('https://shauru.pythonanywhere.com/api/get-dz', json={'day': 2})

pprint(res.json(), indent=4, depth=4)

