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


