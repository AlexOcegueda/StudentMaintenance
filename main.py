#!/usr/bin/env python3
import menu


def main():
    students = [['Bruno', 'Zamora', 20],
                ['Ela', 'Cross', 30],
                ['Amira', 'Hogarth', 45]]

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
