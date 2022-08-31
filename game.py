from player import Player
from ai import AI
from human import Human

class Game:
   def __init__(self,name):
    super().__init__(name)
    self.get_human_player_choice()

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


def number_of_players():
    print('Choose number ')


def game_mode():
    player_choice = input('Would you like Single or Multi-player?')
    print

    #choose gesture
    #choose game mode
    #























