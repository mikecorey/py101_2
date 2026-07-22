grade_str = input("Enter your grade")
grade = float(grade_str)

if 60 >= grade > 70:
    print('you pass')
elif 70 >= grade > 80:
    print('try harder, technically pass')
elif grade > 80:
    print('acceptable')
elif grade > 90:
    print('nice job')


assert grade == 90
