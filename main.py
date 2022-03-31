#!/usr/bin/env python3
import menu

__program_name__ = "Student Maintenance"
__author__ = "Kyle Yates, Alex Ocegueda"
__version__ = "2.0"
__github__ = "https://github.com/AlexOcegueda/StudentMaintenance"


def main():
    students = [['Bruno', 'Mars', 20],
                ['Katy', 'Perry', 30],
                ['Zendaya', 'Maree', 45]]

    while True:
        menu.display_menu()
        command = input('Command: ')
        if command == '1':
            menu.list_students(students)
        elif command == '2':
            menu.add(students)
        elif command == '3':
            menu.delete(students)
        elif command == '4':
            menu.update(students)
        elif command == '5':
            break
        else:
            print('Not a valid command. Please try again.\n')
    print('Bye!')


if __name__ == '__main__':
    main()
