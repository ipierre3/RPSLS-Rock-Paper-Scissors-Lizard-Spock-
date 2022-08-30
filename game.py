from player import Player
from ai import AI
from human import Human
from time import sleep

class Game:
    pass

def welcome_screen():
    print("""\nWelcome to Rock Paper Scissors Lizard Spock\n \nEach match will be best of three games\nUse the number keys to enter your selection\n
Rock crushes Scissors
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock\n""")

welcome_screen()

def number_of_players():
    print('Choose number ')