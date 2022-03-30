import data_valid


def list(students):
    if len(students) == 0:
        print("There are no students in the list.\n")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student[0]} ({student[1]})")
        print()


def add(students):
    name = input("Name: ")
    id = input("ID: ")
    student = [name, id]
    students.append(student)
    print(f"{student[0]} was added.\n")


def delete(students):
    number = int(input("Number: "))
    if number < 1 or number > len(students):
        print("Invalid student id.\n")
    else:
        student = students.pop(number - 1)
        print(f"{student[0]} was deleted.\n")


def update(students):
    num = int(input(f'Enter which student you want to edit:'))
    student_old = students[num - 1]
    data_valid.yes_or_no(f'Are you sure you want to edit {student_old[0]}')
    name = input("Name: ").title()  # make sure students name is Capital
    id = input("ID: ")
    students[int(num) - 1] = (name, id)
    student = students[num - 1]
    print(f'{student_old[0]} was replaced with {student[0]}')


def display_menu():
    print("COMMAND MENU")
    print("1 - List all students")
    print("2 - Add a student")
    print("3 - Delete a student")
    print("4 - Update student")
    print("5 - Exit program")
    print()
