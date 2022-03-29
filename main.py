#!/usr/bin/env python3
import menu


def main():
    students = [["Kyle Yates", 1975],
                ["On the Waterfront", 1954],
                ["Cat on a Hot Tin Roof", 1958]]

    menu.display_menu()

    while True:
        command = input("Command: ")
        if command == "1":
            menu.list(students)
        elif command == "2":
            menu.add(students)
        elif command == "3":
            menu.delete(students)
        elif command == "4":
            menu.update(students)
        elif command == "5":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()
