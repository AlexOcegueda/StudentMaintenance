def list(students):
    if len(students) == 0:
        print("There are no movies in the list.\n")
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
    print("Place holder for later")


def display_menu():
    print("COMMAND MENU")
    print("1 - List all students")
    print("2 -  Add a student")
    print("3 -  Delete a student")
    print("4 - Update student")
    print("4 - Exit program")
    print()
