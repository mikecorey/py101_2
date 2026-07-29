from person import Person

class Instructor(Person):
    def __init__(self, name, phone, email, salary):
        super().__init__(name, phone, email)
        self.salary = salary

    def teaches(self, course):
        raise NotImplementedError

    def display(self):
        super().display()
        print(f'  INSTRUCTOR SPECIFIC: Salary: {self.salary}')
