def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})")
        print()


def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = [name, year]
    movie_list.append(movie)
    print(f"{movie[0]} was added.\n")


def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie[0]} was deleted.\n")


def display_menu():
    print("COMMAND MENU")
    print("1 - List all movies")
    print("2 -  Add a movie")
    print("3 -  Delete a movie")
    print("4 - Exit program")
    print()