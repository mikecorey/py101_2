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
