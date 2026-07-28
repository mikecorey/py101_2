import json
import csv

csv_contacts = []
with open('../sample_data/fake_address_book.csv') as f:
    reader = csv.DictReader(f)
    for record in reader:
        csv_contacts.append(record)

json_contacts = None
with open('../sample_data/fake_address_book.json') as f:
    json_contacts = json.load(f)

print("Does == work?")
print(csv_contacts == json_contacts)

print('What about lens?')
print(len(csv_contacts) == len(json_contacts))

csv_contacts_as_json = set([json.dumps(c) for c in csv_contacts])
for j in json_contacts:
    j['is_favorite'] = str(j['is_favorite']).lower()
json_contacts_as_json = set([json.dumps(j) for j in json_contacts])

print('difference')
print(json_contacts_as_json - csv_contacts_as_json)
