from ai import AI
from human import Human

class Game:
   def __init__(self):
    self.player_one = Human("Player")
    self.player_two = None
    self.rounds = 0


   def run_game(self):
        self.welcome_screen()
        self.number_of_rounds()
        self.game_mode()
        self.compare_gesture()
        self.determine_winner()
        self.play_again()

   def welcome_screen(self):
        print('\nWelcome to Rock Paper Scissors Lizard Spock\n \nGame will be played with a minimum of 3 rounds to decide a winner\nYou will use the number keys to enter your selection')
        print('\nREMEMBER:\n\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

        play = input("Now would you like to play Rock, Paper, Scissors, Lizard, Spock(y/n): ").lower()
        if play == "y":
            print('\nFor selections: ')
            print("\n1 = Rock")
            print("2 = Paper")
            print("3 = Scissors")
            print("4 = Lizard")
            print("5 = Spock")

        elif play == "n":
            print("\nNo worries! Maybe next time")
            self.welcome_screen()

   def number_of_rounds(self):
        self.rounds = int(input('\nHow many rounds do you wish to play?: '))
        while self.rounds < 3:
            print('Sorry! Rounds now defaulted to 3')
            for num_rounds in range(3):
                num_rounds += 1
            return num_rounds
        if self.rounds >= 3:
            for num_rounds in range(int(self.rounds)):
                num_rounds += 1
            return num_rounds
   
   def game_mode(self):
        self.player = input('Would you like Single or Multi-player?: ').lower()
        if self.player == 'single':
            print('You have selected to play against Skynet')
            self.player_two = AI('Skynet')
        elif self.player == 'multi-player':
            print('You have chosen PvP style')
            self.player_two = Human('Player 2')
        else:
            print('Invalid Choice')

   def compare_gesture(self):
    pass
    
       
        
   def determine_winner(self):
        

   def play_again(self):
        while True:
            self.again = input('Would you like to play again? Enter(y/n): ').lower()
            if self.again == 'y':
                self.welcome_screen()
            else:
                print('Thanks for playing!')
                break


