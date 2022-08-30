from player import Player
from ai import AI
from human import Human

class Game:
   def __init__(self,name):
    super().__init__(name)
    self.get_human_player_choice()


def welcome_screen():
    print('Welcome to Rock Paper Scissors Lizard Spock\n \nEach match will be best of three games\nUse the number keys to enter your selection')


def rules_explained():
    print('The rules are as follows:\n Rock crushes Scissors\n Scissors cuts Paper \n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Simple\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock\n The winner will win the best of three rounds.')


def game_mode():
    player_choice = input('Would you like Single or Multi-player?')
    print

    #choose gesture
    #choose game mode
    #























