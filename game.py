from human import Human
from ai import AI

class Game:
   def __init__(self):
    self.player_one = Human("Player 1")
    self.player_two = None
    self.num_rounds = 0


   def run_game(self):
        self.welcome_screen()
        self.number_of_rounds()
        self.game_mode()
        self.chosen_gestures()
        self.compare_gesture()
        self.capture_score()
        self.determine_winner()
        self.play_again()

   def welcome_screen(self):
        print('\nWelcome to Rock Paper Scissors Lizard Spock\n \nGame will be played with a minimum of 3 rounds to decide a winner\nYou will use the number keys to enter your selection')
        print('\nREMEMBER:\n\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

        play = input("Now, would you like to play Rock, Paper, Scissors, Lizard, Spock? Enter (y/n): ").lower()
        if play == "y":
            print('\nFor selections: ')
            print("\n0 = Rock")
            print("1 = Paper")
            print("2 = Scissors")
            print("3 = Lizard")
            print("4 = Spock")
        elif play == "n":
            print("\nNo worries! Maybe next time")
            return self.run_game()

   def number_of_rounds(self):
        self.rounds = int(input('\nHow many rounds do you wish to play?: '))
        while self.rounds < 3:
            print('Sorry! Rounds now defaulted to 3')
            for self.num_rounds in range(3):
                return
        if self.rounds >= 3:
            for self.num_rounds in range(int(self.rounds)):
                return
        else:
            print('Invalid Choice')
            return self.number_of_rounds()

   def game_mode(self):
        self.player = input('\nWould you like Single or Multi-player?: ').lower()
        if self.player == 'single':
            print('\nYou have chosen to play against Skynet')
            self.player_two = AI('Skynet')
        elif self.player == 'multi-player':
            print('\nYou have chosen PvP style')
            self.player_two = Human('Player 2')
        else:
            print('Invalid Choice')
            return self.game_mode()

   def chosen_gestures(self):
        player_one_choice = self.player_one.choose_gesture()
        player_two_choice = self.player_two.choose_gesture()
        
        return self.compare_gesture(player_one_choice, player_two_choice)

   def compare_gesture(self, player_one_choice , player_two_choice):
        if player_one_choice == player_two_choice:
            print("\nIt's a tie.")
            self.num_rounds += 1
        elif player_one_choice == 0 and (player_two_choice == 2 or player_two_choice == 3):
            print("\nPlayer 1 Wins!")
            self.player_one.score += 1
            self.num_rounds += 1
        elif player_one_choice == 1 and (player_two_choice == 0 or player_two_choice == 4):
            print("\nPlayer 1 Wins!")
            self.player_one.score += 1
            self.num_rounds += 1
        elif player_one_choice == 2 and (player_two_choice == 1 or player_two_choice == 3):
            print("\nPlayer 1 Wins!")
            self.player_one.score += 1
            self.num_rounds += 1
        elif player_one_choice == 3 and (player_two_choice == 4 or player_two_choice == 1):
            print("\nPlayer 1 Wins!")
            self.player_one.score += 1
            self.num_rounds += 1
        elif player_one_choice == 4 and (player_two_choice == 2 or player_two_choice == 0):
            print("\nPlayer 1 Wins!")
            self.player_one.score += 1
            self.num_rounds += 1
        else:
            print(f'\n{self.player_two.name} Wins!')
            self.player_two.score += 1
            self.num_rounds += 1

        if self.num_rounds == self.rounds:
            return self.capture_score()
        else:
            return self.chosen_gestures()

   def capture_score(self):
        score1 = self.player_one.score
        score2 = self.player_two.score
        return self.determine_winner()
            
   def determine_winner(self):
        if self.player_one.score > self.player_two.score:
            print(f'\n{self.player_one.name} Wins the Game!')
            return self.play_again()
        elif self.player_one.score < self.player_two.score:
            print(f'\n{self.player_two.name} Wins the Game!')
            return self.play_again()
        elif self.player_one.score == self.player_two.score:
            print ("\nGAME HAS TIED!")
            return self.play_again()

   def play_again(self):
        while True:
            self.again = input('\nWould you like to play again? Enter(y/n): ').lower()
            if self.again == 'y':
                return self.run_game()
            else:
                print('\nThanks for playing!')
            break