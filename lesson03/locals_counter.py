""" local, nonlocal, global"""
name = 'Max'


def a():
    name = 'Vasia'

    def b():
        global name  # nonlocal
        name = 'Petya'
        print(name)

    b()
    print(name)


a()
print(name)

""" counter """


def counter():
    count = 0

    def wrap():
        nonlocal count
        count += 1
        return count

    return wrap


class Student:
    # A student ID counter
    idCounter = 0

    def __init__(self):
        self.gpa = 0
        self.record = {}
        # Each time I create a new student, the idCounter increment
        Student.idCounter += 1
        self.name = 'Student {0}'.format(Student.idCounter)


classRoster = []  # List of students
for number in range(10):
    newStudent = Student()
    classRoster.append(newStudent)
    print(newStudent.name)
