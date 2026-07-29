import random

from course import Course
from student import Student
from instructor import Instructor

def name_gen():
    names = ['alice', 'bob', 'carol', 'dave', 'ernie', 'fred', 'greg', 'henry', 'ivan', 'julie', 'karen']
    last_initial = 'abcdefghijklmnopqrstuvwxyz'
    return random.choice(names) + ' ' + random.choice(last_initial)


courses = []
students = []
instructors = []

c1 = Course('fundamentals of programming', 'cs50')
c2 = Course('intro to programming', 'cs101', max_enrollment=50)
c3 = Course('advanced programming', 'cs201')

e1 = Course('english 101', 'eng101')
e2 = Course('english poetry', 'eng102', max_enrollment=10)

courses = [c1,c2,c3,e1,e2]

students = []
for _ in range(1000):
    new_name = name_gen()
    new_phone = ''.join([str(random.randint(0,9)) for _ in range(10)])
    new_email = new_name.strip().replace(' ', '') + '@example.com'
    new_dorm_num = random.randint(100,599)
    new_student_id = f'STU-{random.randint(10_000, 20_000)}'
    students.append(Student(new_name, new_phone, new_email, new_dorm_num, new_student_id))

instructors = []
for _ in range(10):
    new_name = name_gen()
    new_phone = ''.join([str(random.randint(0,9)) for _ in range(10)])
    new_email = new_name.strip().replace(' ', '') + '@example.com'
    new_salary = random.randint(80_000, 180_000)
    instructors.append(Instructor(new_name, new_phone, new_email, new_salary))



print('-'*40)
print('students')
for s in students[:5]:
    s.display()

print('-'*40)
print('instructors')
for i in instructors[:3]:
    i.display()

for _ in range(10000):
    student = random.choice(students)
    course = random.choice(courses)
    course.enroll_student(student)



print('-'*40)
print('courses')
for c in courses:
    #c.display()
    print(f'{c.name} is over enrolled? {c.is_over_enrolled()}')