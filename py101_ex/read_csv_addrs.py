contacts = []
with open('../sample_data/fake_address_book.csv') as f:
    f.readline()
    for line in f:
        line = line.strip()
        parts = line.split(',')
        name, address, city, state, zip_code, phone, email, is_favorite = parts
        c = {}
        c['name'] = name
        c['address'] = address
        c['city'] = city
        c['state'] = state
        c['zip'] = zip_code
        c['phone'] = phone
        c['email'] = email
        c['is_favorite'] = is_favorite == "true"
        contacts.append(c)

print(f'loaded {len(contacts)} contacts.')
print(contacts[:3])


