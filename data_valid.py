import main


def yes_or_no(prompt):
    """

    :param prompt: Used to tell the user what they are saying yes or no to
    :return: True if they mean yes and False if they mean No

    """

    while True:
        user_input = input(f'{prompt} (y=yes, n=no): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            main.main()
        else:
            print(f'Invalid Input: {prompt}')


def valid_num_range(prompt, high, low):
    """

    :param prompt: Used to tell the user the range and prompt of what they are entering.
    :param high: Enter the highest number that can be entered by users
    :param low: Enter the lowest number that can be entered by users
    :return: a valid number between the ranges specified
    """
    while True:
        user_input = input(f'{prompt} (Valid {low}-{high}: ')

        if type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if low <= number <= high:
            return number
        else:
            print(f'Invalid input')
