import requests
import json

response = requests.get("http://api.open-notify.org/astros")
#print(response.json()['people'])

people = response.json()["people"]

for i in range(0, len(people)):
    text = json.dumps(people[i], sort_keys=True, indent=4)
    print(f"{text}\n\n")

#text = json.dumps(people, sort_keys=True, indent=4)
#print(text)
#for i in range(0, len())