def add_student(students, name):
    students.append(name)

def show_students(students):
    for name in students:
        print(name)

students = []
n = int(input("How many students? "))
for i in range(n):
    name = input("Name: ")
    add_student(students, name)

show_students(students)
