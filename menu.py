def list(students):
    if len(students) == 0:
        print("There are no movies in the list.\n")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student[0]} ({student[1]})")
        print()


def add(students):
    name = input("Name: ")
    year = input("Year: ")
    student = [name, year]
    students.append(student)
    print(f"{student[0]} was added.\n")


def delete(students):
    number = int(input("Number: "))
    if number < 1 or number > len(students):
        print("Invalid student id.\n")
    else:
        student = students.pop(number - 1)
        print(f"{student[0]} was deleted.\n")


def display_menu():
    print("COMMAND MENU")
    print("1 - List all movies")
    print("2 -  Add a movie")
    print("3 -  Delete a movie")
    print("4 - Exit program")
    print()