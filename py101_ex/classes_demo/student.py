from person import Person

class Student(Person):
    def __init__(self, name, phone, email, dorm_num, student_id):
        super().__init__(name, phone, email)
        self.dorm_num = dorm_num
        self.student_id = student_id

    def display(self):
        super().display()
        print(f'  STUDENT SPECIFIC: Dorm: {self.dorm_num}, student_id: {self.student_id}')