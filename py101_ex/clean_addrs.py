import csv

def is_valid_state(state_str):
    return len(state_str) == 2


REQUIRED_FIELDS = set(['name', 'address', 'city', 'state', 'zip', 'phone', 'email', 'is_favorite'])
def is_valid_contact(record):
    available_keys = set(record.keys())
    if len(REQUIRED_FIELDS - available_keys) > 0:
        print('missing required field for record:')
        print(record)
        return False
    else:
        if not is_valid_state(record['state']):
            print("invalid state for record")
            print(record)
        else:
            return True


def normalize_contact(record):
    normalized_record = {k.lower(): v for k,v in record.items()}
    normalized_record['state'] = normalized_record['state'][:2]
    return normalized_record

def read_clean_contacts_from_file(fn):
    contacts = []
    with open(fn) as f:
        reader = csv.DictReader(f)
        for record in reader:
            normalized_record = normalize_contact(record)
            is_valid = is_valid_contact(normalized_record)
            if is_valid:
                contacts.append(normalized_record)
            else:
                print("invalid contact:")
                print(normalized_record)
    return contacts
    

def process_contact(contact):
    return {k: v.lower() for k,v in contact.items()}




def write_contacts(contacts):
    with open('../sample_data/cleaned_contacts.csv', 'w') as f:
        writer = csv.DictWriter(f, contacts[0].keys())
        writer.writeheader()
        writer.writerows(contacts)


contacts = read_clean_contacts_from_file('../sample_data/fake_address_book.csv')
processed_contacts = [process_contact(c) for c in contacts]
write_contacts(processed_contacts)
