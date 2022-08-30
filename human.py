from player import Player


class Human(Player):
    
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gestures(self):
        self.choosen_gesture = input('Use the number keys to enter your selection')
        
