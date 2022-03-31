from data_valid import valid_num_range
from data_valid import yes_or_no


def list_students(students):
    """
    Shows all students which are in the list; displaying their full name and student ID
    :param students: List of stored students
    """
    if len(students) == 0:
        print('There are no students in the list.\n')
    else:
        for i, student in enumerate(students, start=1):
            print(f'{i}. Name: {student[0]:<5} {student[1]:<8} ID: {student[2]}')
        print()


def add(students):
    """
    Adds a new student to the list of students by taking in their full name and ID
    :param students: List of stored students
    """
    first = input('First: ')
    last = input('Last: ')
    student_id = input('ID: ')
    student = [first, last, student_id]
    students.append(student)
    print(f'{student[0]} was added.\n')


def delete(students):
    """
    Removes student from list of students
    :param students: List of stored students
    """
    number = int(input('Number: '))
    if number < 1 or number > len(students):
        print('Invalid student id.\n')
    else:
        student = students.pop(number - 1)
        print(f'{student[0]} was deleted.\n')


def update(students):
    """
    Replace student a specified index, and give the option to skip each of them.
    If user does not want to change chosen student it will redirect them back
    to the main menu.
    :param students: 2D list where to store students
    :return:
        Print previous student and their replacement.
    """
    num = int(valid_num_range("Which student do you want to edit? ", len(students), 1))
    student_old = students[num - 1]
    print()

    if yes_or_no(f'Are you sure you want to edit {student_old[0]}'):
        print('='*20)
        print(f'Enter new credentials or Press enter to keep previous!')
        first = str(input('First name: ').title())  # make sure students name is Capital
        last = input('Last name:').title()
        student_id = input('ID: ')
        # check if they entered skip
        if first == '':
            first = student_old[0]
        if last == '':
            last = student_old[1]
        if student_id == '':  # check for both as no .title() their id
            student_id = student_old[2]
        students[int(num) - 1] = (first, last, student_id)
        print(f'{student_old[0]} was replaced with {first}, {last}, {student_id}')
        print('')


def display_menu():
    print('='*20)
    print(f'{"":>4}COMMAND MENU')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Delete a student')
    print('4 - Update student')
    print('5 - Exit program')
    print('=' * 20)
    print()
