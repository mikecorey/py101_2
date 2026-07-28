contacts = []
with open('../sample_data/fake_address_book.csv') as f:
    headers = f.readline().strip().split(',')
    for line in f:
        line = line.strip()
        parts = line.split(',')
        name, address, city, state, zip_code, phone, email, is_favorite = parts
        c = dict(zip(headers, parts))
        c['is_favorite'] = is_favorite == "true"
        contacts.append(c)

print(f'loaded {len(contacts)} contacts.')
print(contacts[:3])


