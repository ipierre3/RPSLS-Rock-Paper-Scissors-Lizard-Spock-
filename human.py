from player import Player


class Human(Player):
    
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.gestures = ['Rock', 'Paper', "Scissors", 'Lizard', "Spock"]
        self.chosen_gesture = int(input('\nPlayer Choose your weapon: '))
        while True:
            if self.chosen_gesture > 4:
                print("Invalid choice. Please choose again")
                self.choose_gesture()
            elif self.chosen_gesture < 0:
                print("Invalid choice. Please choose again")
                self.choose_gesture()
            elif self.chosen_gesture == 0:
                print("You picked Rock")
            elif self.chosen_gesture == 1:
                print("You picked Paper")
            elif self.chosen_gesture == 2:
                print("You picked Scissors")
            elif self.chosen_gesture == 3:
                print("You picked Lizard")
            elif self.chosen_gesture == 4:
                print("You picked Spock")
            return self.chosen_gesture
