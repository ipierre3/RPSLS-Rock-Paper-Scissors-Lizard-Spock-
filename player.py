

class Player:
    def __init__(self):
        self.score = 0
        self.gestures = ['Rock', 'Paper', "Scissors", 'Lizard', 'Spock']

    def win_round(self):
        self.score += 1

    def choose_gesture(self):
        pass