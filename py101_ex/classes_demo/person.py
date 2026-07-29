class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f'PERSON: Name: {self.name}, Phone: {self.phone},  Email: {self.email}')