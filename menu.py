from data_valid import valid_num_range
from data_valid import yes_or_no
from data_valid import continue_message

__program_name__ = "Student Maintenance"
__author__ = "Kyle Yates, Alex Ocegueda"
__version__ = "2.0"
__github__ = "https://github.com/AlexOcegueda/StudentMaintenance"


line = f'\t{"=" * 15}'  # for print line/formatting


def list_students(students):
    """
    Shows all students which are in the list; displaying their full name and student ID
    :param students: List of stored students
    """
    if len(students) == 0:  # checks if list is empty
        print('There are no students in the list.\n')
    else:
        # print students list
        for i, student in enumerate(students, start=1):
            print(f'\t{i}. Name: {student[0]:<9} {student[1]:<8} ID: {student[2]}')
        continue_message()
        print()


def add(students):
    """
    Adds a new student to the list of students by taking in their full name and ID
    :param students: List of stored students
    """
    print(line)  # print format line
    print(f'\tAdd Student')
    first = input(f'\tFirst: ')  # user enters first name
    last = input(f'\tLast: ')  # user enters last name
    student_id = input(f'\tID: ')  # user enters id
    student = [first, last, student_id]
    students.append(student)  # add student to the list
    print(f'\t{student[0]} was added.')
    continue_message()


def delete(students):
    """
    Removes student from list of students.
    param students: List of stored students
    """

    if len(students) != 0:  # checks if list is empty
        number = int(valid_num_range(f"\tWhich student do you want to delete", len(students), 1))
        student = students[number - 1]
        if yes_or_no(f'\tAre you sure you want to delete {student[0]} {student[1]}'):
            if number < 1 or number > len(students):
                print('Invalid student id.\n')
            else:
                student = students.pop(number - 1)
                print(f'\t{student[0]} was deleted.\n')
                continue_message()
                return
        else:  # reaches here if they entered no
            print(f"\tReturning back to main menu")
            continue_message()
    else:  # reaches here if the list was emtpy
        print(f'\tNo students in list, returning..')
        continue_message()


def update(students):
    """
    Replace student a specified index, and give the option to skip each of them.
    If user does not want to change chosen student it will redirect them back
    to the main menu.
    param students: 2D list where to store students
    :return:
        Print previous student and their replacement.
    """
    if len(students) != 0:  # checks if list is emtpy
        print(f'\t{"Update Student":>10}')
        print(f'\t{"-" * 15}')
        num = int(valid_num_range(f"\tWhich student do you want to edit? ", len(students), 1))
        student_old = students[num - 1]
        print()
        # question to ask if the student their editing is correct
        if yes_or_no(f'\tAre you sure you want to edit {student_old[0]}'):
            print(f'\t{"=" * 15}')
            # user input
            print(f'\tEnter new credentials or Press enter to keep previous!')
            first = str(input(f'\tFirst name: ').title())  # make sure students name is Capital
            last = input(f'\tLast name: ').title()
            student_id = input('\tID: ')

            # check if they entered anything
            if first == '':
                first = student_old[0]
            if last == '':
                last = student_old[1]
            if student_id == '':  # check for both as no .title() their id
                student_id = student_old[2]

            students[int(num) - 1] = (first, last, student_id)
            print(f'\t{student_old[0]} was replaced with {first}, {last}, {student_id}')
            continue_message()
            print()
        else:
            print("\tCancelling update..")
            print()
            return
    else:
        print(f'\tNo students in list, returning..')
        return


def display_menu():
    """
    Display a menu that the user gets to select from (1-5).
    :return:
        Print menu items.
    """
    print('=' * 20)
    print(f'{"":>4}COMMAND MENU')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Delete a student')
    print('4 - Update student')
    print('5 - Exit program')
    print('=' * 20)
    print()
