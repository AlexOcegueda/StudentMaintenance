__program_name__ = "Student Maintenance"
__author__ = "Kyle Yates, Alex Ocegueda"
__version__ = "2.0"
__github__ = "https://github.com/AlexOcegueda/StudentMaintenance"


def yes_or_no(prompt):
    """
    Yes or no prompt, where prompt is the message wished to be displayed.
    If yes, return true and continue, if no return false.

    param prompt: Used to tell the user what they are saying yes or no to
    :return: True if they mean yes and False if they mean No
    """
    while True:
        user_input = input(f'{prompt} (y=yes, n=no): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print(f'Invalid Input: {prompt}')


def valid_num_range(prompt, high, low):
    """
    A data validation where you specify the prompt, along with the high and low ranges
    that the user can select from.

    param prompt: Used to tell the user the range and prompt of what they are entering.
    param high: Enter the highest number that can be entered by users
    :param prompt: function defined prompt for valid num range
    :param high: Enter the highest number that the user can enter.
    :param low: Enter the lowest number that can be entered by users
    :return: a valid number between the ranges specified
    """
    while True:
        user_input = input(f'{prompt} (Valid {low}-{high}): ')  # user input of number between range

        if type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if low <= number <= high:   # checks if between range
            return number
        else:
            print(f'Invalid input')


def continue_message():
    """
    Simple function to print continue message.
    Prevents storing anything other than space.
    :return:
        Empty character
    """
    userinput = input(f'\tPress enter to continue')
    if userinput == "":
        return userinput
    else:
        userinput = ''
        return userinput
