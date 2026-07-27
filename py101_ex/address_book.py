contacts = []

# Add a contact
mike_contact = {
    "name": "Mike",
    "phone": "123-456-7890",
    "email": "mike@example.com"
}
contacts.append(mike_contact)

# Add another contact
matt_contact = {
    "name": "Matt",
    "phone": "987-654-3210",
    "email": "matt@example.com"
}
contacts.append(matt_contact)

alice_contact = {
    "name": "Alice",
    "phone": "555-123-4567",
    "email": "alice@example.com"
}
contacts.append(alice_contact)

bob_contact = {
    "name": "Bob",
    "phone": "555-987-6543",
    "email": "bob@example.com"
}
contacts.append(bob_contact)

carol_contact = {
    "name": "Carol",
    "phone": "555-555-1234",
    "email": "carol@example.com"
}
contacts.append(carol_contact)

doug_contact = {
    "name": "Doug",
    "phone": "555-555-5678",
    "email": "doug@example.com"
}
contacts.append(doug_contact)

eve_contact = {
    "name": "Eve",
    "phone": "555-555-8765",
    "email": "eve@example.com"
}
contacts.append(eve_contact)

# Add a bad contact
bad_contact = {
    "name": "Bad Contact",
    "phone": "555-555-5555",
    "email": "bad@example.com"
}
contacts.append(bad_contact)

# Print all contacts
for contact in contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}") 

print("\nUpdating Mike's contact information...\n")
mike_contact['name'] = "Michael"

# Print all contacts
for contact in contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

print("\nRemoving Bad Contact...\n")
contacts.remove(bad_contact)

# Print all contacts
for contact in contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}") 

mike_contact['is_favorite'] = True
bob_contact['is_favorite'] = True
eve_contact['is_favorite'] = True
matt_contact['is_favorite'] = True

for f in contacts:
    if 'is_favorite' in f and f['is_favorite']:
        print(f"{f['name']} is a favorite contact.")



def search_contact(search_str, contacts):
    return [c for c in contacts if 'name' in c and search_str in c['name']]

def set_favorite(contact, is_favorite=True):
    contact['is_favorite'] = is_favorite
    
print('before fight')
print(matt_contact)

set_favorite(matt_contact, False)
print('after fight')
print(matt_contact)

set_favorite(matt_contact)

print('make ammends')
print(matt_contact)

def count_favs(contacts):
    return count([c for c in contacts if 'is_favorite' in c and c['is_favorite']])

def set_email(contact, email_str):
    if '@' in email_str and '.' in email_str:
        contact['email'] = email_str
    else:
        print('invalid email')

def get_domains_in_email(contacts):
    return set([c['email'].split('@')[-1] for c in contacts if 'email' in c])

def set_addr_state(contact, addr_state):
    addr_state = addr_state.strip().upper()
    if len(addr_state) == 2:
        contact['addr_state'] = addr_state
    else:
        print("bad state")
