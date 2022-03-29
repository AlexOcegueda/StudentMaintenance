def yes_or_no():
    prompt = "Enter yes or no"

    while True:
        user_input = input(f'{prompt} (y=yes, n=no): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print('Invalid Input: Please enter yes or no (y=yes, n=no)')
