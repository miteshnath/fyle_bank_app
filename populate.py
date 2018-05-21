import csv
import requests
import json
import pprint

csvfile = open('populate.csv', 'r')
fieldnames = ("ifsc", "bank_id", "branch", "address", "city", "district", "state", "bank_name")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    try:
        r = requests.post('http://127.0.0.1:8000/banks', json=row)
        pprint.pprint(row)
    except Exception as e:
        print(e)
