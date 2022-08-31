from secrets import choice
from player import Player
from ai import AI
from human import Human

class Game:
   def __init__(self):
    self.human = Human("Player")
    self.ai = AI("Skynet")
    self.rounds = 0


   def run_game(self):
        self.welcome_screen()
        self.number_of_rounds()
        self.game_mode()
        self.compare_gesture()
        self.determine_winner()
        self.play_again()

   def welcome_screen(self):
        print('\nWelcome to Rock Paper Scissors Lizard Spock\n \nEach match will be best of three games\nYou will use the number keys to enter your selection')
        print('\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

        play = input("Now would you like to play Rock, Paper, Scissors, Lizard, Spock(y/n): ").lower()
        if play == "y":
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Lizard")
            print("5. Spock")

        elif play != "n":
            print("Error: Please type y for yes or n for no:")

   def number_of_rounds(self):
        self.rounds = int(input('How many rounds do you wish to play?: '))
        while self.rounds < 0:
            for num_rounds in range(3):
                print(f'The game will run for {int(self.rounds)} rounds')           # is not printing // need to figure out why
                num_rounds += 1
            return num_rounds
   
   def game_mode(self):
        self.player = input('Would you like Single or Multi-player?: ')
        if self.player == 'single':
            print('You have selected to play against Skynet')
            self.player_1 = Human('Player')
            self.skynet = AI('Skynet')
        elif self.player == 'Multi-player':
            print('You have chosen PvP style')
            self.player_1 = Human('Player 1')
            self.player_2 = Human('Player 2')
        else:
            print('Invalid Choice')

        # while True:
            
   

#    def compare_gesture(self, human, ai):
#     Pass
       
        
#    def determine_winner(self):
#         if self.human == self.ai:
#             print('Tie')
#         elif self.human > self.ai:
#             print('Player Wins')
#         else:
#             print('AI Wins')

#    def play_again(self):
#         while True:
#             self.play_again = input('Would you like to play again? Enter(y/n): ').lower()
#             if play_again != 'y':
#                 break

#         print('Thanks for playing!')


