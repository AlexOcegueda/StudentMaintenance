#!/usr/bin/env python3
from data_valid import valid_num_range
from student_maint import add
from student_maint import display_menu
from student_maint import delete
from student_maint import update
from student_maint import list_students

"""
Main module to call other functions in different modules to manage
and maintain student lists.
"""
__program_name__ = "Student Maintenance"
__author__ = "Kyle Yates, Alex Ocegueda"
__version__ = "2.0"
__github__ = "https://github.com/AlexOcegueda/StudentMaintenance"


def main():
    """
    Main method used to print menu and take user input.
    :return:
        Menu and their desired command.
    """

    while True:
        # display menu
        display_menu()
        # Check what command they entered.
        command = int(valid_num_range('Command', 5, 1))
        if command == 1:
            list_students()
        elif command == 2:
            add()
        elif command == 3:
            delete()
        elif command == 4:
            update()
        elif command == 5:
            break
        else:
            print('Not a valid command. Please try again.\n')
    print('Bye!')


if __name__ == '__main__':
    main()
