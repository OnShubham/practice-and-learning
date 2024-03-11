# Object Oriented Programmig (OOP)

# # Class
# class PlayerCharacter:  # this is class
#     pass


# class player:
#     def __init__ (self, name, age):
#         self.name = name # attributes
#         self.age = age  # attributes

#     def store(self):
#         return 'done'

#     playes1 = player('shubham', 21)
#     playes2 = player('Nikhil', 21)

#     print(playes1)
#     print(playes2)


# Player Program

class Player:
    memebership = True

    def __init__(self, name, age):

        if (Player.memebership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name} and my age {self.age}')


# Instantiating player objects outside the class definition
player1 = Player('shubham', 21)
player2 = Player('Nikhil', 21)


# Calling the shout method for each player
print(player1.shout())
print(player2.shout())


# Marks add a Program

class Score:
    def __init__(self, Ot, Ai, Python):
        self.Ot = Ot
        self.Ai = Ai
        self.Python = Python

    def marks(self):
        print(f'Ot Marks = {self.Ot}')
        print(f'Ai Marks = {self.Ai}')
        print(f'Python Marks = {self.Python}')


# Creating instances of the Score class with marks
scores = Score(20, 21, 25)

# Calling the marks method to display the marks
scores.marks()


class College:
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    def details(self):
        College_name = {
            'name': 'Dy patil',
            'branch': 'Computer',
            'year': 2021
        }

# Inheritance


