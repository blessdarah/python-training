import random

# game class
class Game:
    def __init__(self, max_range=6, wining_points=30) -> None:
        self.p1_points = 0
        self.p2_points = 0
        self.wining_points = wining_points
        self.active_player = 1
        self.hasWinner = False
        self.max_random_range = max_range

    def set_points(self, points):
        if(self.active_player == 1):
            self.p1_points += points
        else:
            self.p2_points += points

    def role(self):
        # generate a random number between 1 and 6
        role_number = random.randint(1, self.max_random_range)
        self.set_points(role_number) 

        print(f"Roled {role_number} for player {self.active_player}")
        self.switch_player()
        self.check_winner()

    def switch_player(self):
        if(self.active_player == 1):
            self.active_player = 2
        else:
            self.active_player = 1

    def check_winner(self):
        if(self.p1_points >= self.wining_points):
            print("P1 is the winner with", self.p1_points, " points")
            self.hasWinner = True

        if(self.p2_points >= self.wining_points):
            print("P2 is the winner with", self.p2_points, " points")
            self.hasWinner = True



# Shooter is game
class Shooter(Game):
    def __init__(self, max_range=10, wining_points=100) -> None:
        super().__init__(max_range, wining_points)
    
    def role(self):
        random_number = random.randint(1, self.max_random_range)
        if(random_number % 2 == 0):
            third = int(random_number / 3)
            self.set_points(third)
        else: 
            self.set_points(random_number)
        
        self.check_winner()
        self.switch_player()

# Start the game logic
game = Shooter(max_range=50, wining_points=500)
while (not game.hasWinner):
    game.role()

