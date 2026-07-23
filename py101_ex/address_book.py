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

