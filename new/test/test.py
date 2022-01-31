from flask import json
import requests

BASE = "http://localhost:3000/getLoan"

response = requests.delete(BASE)

response = requests.get(BASE)
print('after deletion of DB',response.json())

with open('test.json', 'r') as file:
    test_data = json.load(file)

    for entries in test_data:
        response = requests.post(BASE, entries)
        print(response.json())

with open('update.json','r') as file:
    update_test_data = json.load(file)
    for update in update_test_data:
        response = requests.put(BASE,entries)

response = requests.get(BASE)
print(response.json())

