#!/usr/bin/env python3
from data_valid import yes_or_no
from data_valid import continue_message

"""
Functions needed to add, delete, update and display for the main module
"""
__program_name__ = "Student Maintenance"
__author__ = "Kyle Yates, Alex Ocegueda"
__version__ = "2.0"
__github__ = "https://github.com/AlexOcegueda/StudentMaintenance"

# Variables and list needed
line = f'\t{"=" * 15}'  # for print line/formatting
students = [[1, 'Bruno', 'Mars'],
            [2, 'Katy', 'Perry'],
            [3, 'Zendaya', 'Maree']]
id_num = len(students) + 1


def list_students():
    """
    Shows all students which are in the list; displaying their full name and student ID
    """
    if len(students) == 0:  # checks if list is empty
        print('There are no students in the list.\n')
    else:
        # print students list
        for i, student in enumerate(students, start=1):
            print(f'\tID: {student[0]:<2} Name: {student[1]:<8} {student[2]}')
        continue_message()
        print()


def add():
    """
    Adds a new student to the list of students by taking in their full name and ID
    """
    print(line)  # print format line
    print(f'\tAdd Student')
    first = input(f'\tPlease enter the Students First Name:')  # user enters first name
    last = input(f'\tPlease enter the Students Last Name:')  # user enters last name
    print("Student ID #" + str(id_num), first, last, 'was added.')
    student = [id_num, first, last]
    students.append(student)  # add student to the list
    print(f'\t{student[0]} was added.')
    continue_message()


def delete():
    """
    Removes student from list of students.
    """
    if len(students) != 0:  # checks if list is empty
        id_number = int(input(f"\tSelect the student id you want to delete:"))
        for student in students:
            if id_number == student[0]:
                if yes_or_no(f'\tAre you sure you want to delete {student[0]} {student[1]}'):
                    student = students.pop()
                    print(f'\t{student[0]} was deleted.\n')
                    continue_message()
                    display_menu()
                else:  # reaches here if they entered no
                    print(f"\tReturning back to main menu")
                    continue_message()
    else:  # reaches here if the list was emtpy
        print(f'\tNo students in list, returning..')
        continue_message()
        return


def update():
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
        num = int(input(f"\tWhich student do you want to edit? "))
        student_old = students[num - 1]
        print()
        # question to ask if the student their editing is correct
        for i in students:
            if num == i[0]:
                if yes_or_no(
                        f'\tDo you want to update student ID #, {student_old[0]} {student_old[1]} {student_old[2]}'):
                    print(f'\t{"=" * 15}')
                    # user input
                    print(f'\tEnter new credentials or Press enter to keep previous!')
                    first = str(input(f'\tFirst name: ').title())  # make sure students name is Capital
                    last = input(f'\tLast name: ').title()

                    if first == '':
                        first = student_old[1]
                    if last == '':
                        last = student_old[2]
                else:
                    print("\tCancelling update..")
                    print()
                    return
                students[num - 1] = (i[0], first, last)
                print(f'\t{student_old[1]} {student_old[2]} was updated with {first}, {last}')
                continue_message()
                print()

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
