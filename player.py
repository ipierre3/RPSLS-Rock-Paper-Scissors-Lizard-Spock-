class Player:
    def __init__(self):
        pass

    def gethumanPlayerChoice():
        choice = int(input('Choose your weapon: '))
        while True:
            if choice > 5:
                print("Invalid choice. Please choose again")
            elif choice < 1:
                print("Invalid choice. Please choose again")
            elif choice == 1:
                print("You picked Rock")
            elif choice == 2:
                print("You picked Paper")
            elif choice == 3:
                print("You picked Scissors")
            elif choice == 4:
                print("You picked Lizard")
            elif choice == 5:
                print("You picked Spock")
            return choice