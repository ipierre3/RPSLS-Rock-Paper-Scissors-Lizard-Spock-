from player import Player
from ai import AI
from human import Human

class Game:
<<<<<<< HEAD
   def __init__(self):
    self.human = Human("Player 1")
    self.ai = AI("Skynet")


   def run_game(self):
        self.welcome_screen()
        self.game_mode()
        self.number_of_rounds()
        self.chosen_gesture()
        self.determine_winner()
        self.play_again()

   def welcome_screen(self):
        print('\nWelcome to Rock Paper Scissors Lizard Spock\n \nEach match will be best of three games\nYou will use the number keys to enter your selection')
        print('\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')
=======
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

>>>>>>> 2e800b6de91b492bc10daf6eaeb19d683d6ec2cc

        play = input("Now would you like to play Rock, Paper, Scissors, Lizard, Spock(y/n): ").lower()
        if play == "y":
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Lizard")
            print("5. Spock")

        elif play != "n":
            print("Error: Please type y for yes or n for no:")

#    def game_mode(self):
#         self.player = input('Would you like Single or Multi-player?: ')
#             if self.player = 'single"
#             pass
    

   def number_of_rounds(self):
        rounds = int(input('How many rounds do you wish to play?: '))
        for number in range(rounds):
            player = self.player_gesture()
            ai = self.ai_gesture()
            

   def chosen_gesture(self, human, ai):
        pass
       
        


<<<<<<< HEAD
   def determine_winner(self):
        if self.human == self.ai:
            print('Tie')
        elif self.human > self.ai:
            print('Player Wins')
        else:
            print('AI Wins')
=======
def game_mode():
    player_choice = input('Would you like Single or Multi-player?')
    print
>>>>>>> 2e800b6de91b492bc10daf6eaeb19d683d6ec2cc

   def play_again(self):
        while True:
            self.play_again = input('Would you like to play again? Enter(y/n): ').lower()
            if play_again != 'y':
                break

        print('Thanks for playing!')























