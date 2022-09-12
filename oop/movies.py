"""
Program to create and manage movies like in netflix using python OOP
title: movies.py
author: Bless Darah
date: Sep 11, 2022
"""

"""
Movie class description
- title
- synopsis
- genre
    - name
    - description

- type:
    single
    series

- director
    - name
    - date of birth
    - bio
"""

# Global variables
genres = []
movies =[]
directors = []

class Movie:
    def __init__(self, title, director, genre="action", synopsis="none"):
        self.title = title
        self.director = director
        self.genre = genre
        self.synopsis = synopsis

    def about(self):
        print(f"Title: {self.title}[{self.genre}]")
        print(f"synopsis: {self.synopsis}")
        


class SingleMovie(Movie):
    def __init__(self, title, director, genre="action", synopsis="none"):
        super().__init__(title, director, genre, synopsis)


class SeasonMovie(Movie):
    def __init__(self, title, director, genre="action", synopsis="none", seasons=1):
        super().__init__(title, director, genre, synopsis)
        self.seasons = seasons


class Director:
    def __init__(self, name, dob, bio=""):
        self.name = name
        self.dob = dob
        self.bio = bio
    
    def info(self):
        print(f"{self.name}, [{self.dob}]")
        print("Bio:", self.bio)
        

class Genre:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def info(self):
        print(f"Title: {self.name}")
        print("Description:", self.description)


def greetings():
    print("Hello welcome to our movie database.")
    user_name = input("Please tell us your name: ")
    print("Welcome", user_name, "what would you like to do?")

    instructions()

def print_genres():
    print("=============== Genres ===============")
    for genre in genres:
        genre.info()

def handle_create_genre() -> Genre:
    name = input("Genre name: ")
    description = input("Description (eg: action movies): ")
    new_genre = Genre(name, description)
    return new_genre

def handle_create_movie():
    pass

def handle_create_director():
    pass

def instructions():
    print("[1]: To create a new movie")
    print("[2]: To create a new movie genre")
    print("[3]: To create a new director")
    print("any other key to quit")
    
    try:
        user_choice = int(input("Enter your choice: "))

        if(user_choice == 1):
            print("Creating user")
            handle_create_movie()
        elif(user_choice == 2):
            print("Creating genre")
            genre = handle_create_genre()
            genres.append(genre) # Add new genre to the genres list (global var)
            print_genres()
        elif(user_choice == 3):
            print("Creating director")
            handle_create_director()

    except ValueError: 
        print("Quiting the application")
    finally:
        print("come back some other time")

def init():
    greetings()
    

# Application entry point
init()
