from player import Player


class Human(Player):
    
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.gestures = ['Rock', 'Paper', "Scissors", 'Lizard', "Spock"]
        self.chosen_gesture = int(input(f'\n{self.name} Choose your weapon: '))
        while True:
            if self.chosen_gesture > 4:
                print("Invalid choice. Please choose again")
                self.choose_gesture()
            elif self.chosen_gesture < 0:
                print("Invalid choice. Please choose again")
                self.choose_gesture()
            elif self.chosen_gesture == 0:
                print(f"{self.name} has picked Rock")
            elif self.chosen_gesture == 1:
                print(f"{self.name} has picked Paper")
            elif self.chosen_gesture == 2:
                print(f"{self.name} has picked Scissors")
            elif self.chosen_gesture == 3:
                print(f"{self.name} has picked Lizard")
            elif self.chosen_gesture == 4:
                print(f"{self.name} has picked Spock")
            return self.chosen_gesture
