# Author: YuekunElla

# Description: This class Point represents a Point with x and y coordinates.
class Point:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.score = self.get_score()

    def get_score(self):
        distance = self.distance_from_zero()
        if distance <= 1:
            return 100
        elif distance > 1 and distance <= 2:
            return 50
        elif distance > 2 and distance <= 3:
            return 20
        elif distance > 3 and distance <= 4:
            return 10
        elif distance > 4:
            return 0

    def distance_from_zero(self):
        import math
        return math.sqrt((self.coord_x - 0)**2 + (self.coord_y - 0)**2) 
        
    def __str__(self):
        return '(' +str(self.coord_x) + ', '+str(self.coord_y)+')'

    
# Description: This class represents a player in the Dart Game.
import math
class Player:
    def __init__(self, name, seed_num = 30):
        import random
        self.seed_num = seed_num
        random.seed(self.seed_num) 
        self.name = name
        self.points = []

    def make_throw(self):
        import random
        num_1 = random.randrange(-5, 6)
        num_2 = random.randrange(-5, 6)
        point = Point(num_1, num_2)
        self.points.append(point)
        print(self.name + ': ' + 'The score for a dart throw at position {} is {}.'.format(point, point.get_score()))
       
    def get_score(self):
        score = self.points[-1].get_score()
        return score

    def get_total_score(self):
        total= 0
        for point in self.points:
            total += point.get_score()
        return str(total) 

    def get_name(self):
        return self.name
    
    def __str__(self):
        print ("{}'s total score is {}.".format(self.name, self.get_total_score()))
        return '\n'.join('The score for a dart throw at position {} is {}.'.format(point, point.get_score()) for point in self.points)

# Description: The class DartGame represents the Dart Game. 
class DartGame:
    def __init__(self, seed_num = 30, max_score = 51):
        self.seed_num = seed_num
        print('***********************************************')
        print('Welcome to the simplified dart game simulation!')
        print('***********************************************')
        self.player1 = self.get_player1()
        self.player2 = self.get_player2()
        self.player1 = Player(self.player1, self.seed_num)
        self.player2 = Player(self.player2, self.seed_num)
        self.max_score = max_score 
        self.rounds = 0
        
    def get_player1(self):
        result = input("Enter player1 name: ")
        while result == "":
            result = input("Enter player1 name: ")
        return result

    def get_player2(self):
        result = input("Enter player2 name: ")
        while result == "":
            result = input("Enter player2 name: ")
        return result

    def play_game(self):
        print()
        self.total_score1 = 0
        self.total_score2 = 0
        self.player1.make_throw()
        self.player2.make_throw()
        self.total_score1 += self.player1.get_score()
        self.total_score2 += self.player2.get_score()
        self.rounds += 1
        while self.total_score1 <= self.max_score  and self.total_score2 <= self.max_score :
            self.player1.make_throw()
            self.player2.make_throw()
            self.rounds += 1
            self.total_score1 += self.player1.get_score()
            self.total_score2 += self.player2.get_score()

    def congratulate_player(self):
        if self.total_score1 == self.total_score2:
            print('***********')
            print("It's a tie!")
            print('***********')
            
        elif self.total_score1 >= self.total_score2:
            prompt = "*" * (32 + len(self.player1.name))
            print(prompt)
            print('Congratulations! The winner is {}.'.format(self.player1.name))
            print(prompt)
            
        elif self.total_score1 <= self.total_score2:
            prompt = "*" * (32 + len(self.player2.name))
            print(prompt)
            print('Congratulations! The winner is {}.'.format(self.player2.name))
            print(prompt)
        print('The number of rounds required is {}.'.format(self.rounds))
        print('The total score of {} is {}.'.format(self.player1.name, self.total_score1))
        print('The total score of {} is {}.'.format(self.player2.name, self.total_score2))

	
game = DartGame(40, 201) #test case
game.play_game()
game.congratulate_player()
