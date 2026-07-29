class Course:
    def __init__(self, name, id, max_enrollment=30):
        self.name = name
        self.id = id
        self.max_enrollment = max_enrollment
        self.__enrolled_students = set()

    def display(self):
        print(f'COURSE: Name: {self.name}, ID: {self.id}, Max_enroll: {self.max_enrollment}')
        print(f'   Students: ')
        for s in self.__enrolled_students:
            s.display()

    def enroll_student(self, student):
        if not self.is_over_enrolled():
            self.__enrolled_students.add(student)

    def has_student_enrolled(self, student):
        return student in self.__enrolled_student

    def is_over_enrolled(self):
        return len(self.__enrolled_students) > self.max_enrollment