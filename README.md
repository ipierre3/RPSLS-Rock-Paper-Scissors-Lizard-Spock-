# RPSLS (Rock-Paper-Scissors-Lizard-Spock)
Python (Git/GitHub, VS Code w/Debugger)

"" Main Stories
 
As a developer, I want to make at least 10 commits with descriptive messages.
As a developer, I want to find a way to properly incorporate inheritance into my game.
As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.
As a developer, I want to store all of the gesture options/choices in a List (AS STRINGS). I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).
As a player, I want the correct player to win a given round based on the choices made by each player.  See below for game rules!
As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner. 
As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.""


"" RPSLS Design

Algorithm

1. Display a welcome message -----> Game class
2. Explain the rules -----> Game class
3. Choose game mode - single player (Human vs. AI) or multiplayer 
(Human vs. Human) -----> Game class
4. Choose number of rounds (but make sure it’s at least 3) -----> Game class
5. Player One chooses Gesture -----> for Player class
6. Player Two chooses Gesture -----> for Player class
7. Compare the gestures -----> Game class
8. Determine winner of the round -----> Game class
    a. Account for ties
9. Determine if the GAME itself has been won -----> Game Class
    a. If it has not, repeat steps 5-9
10. If the game has been won, display the winner, and end the game -----> Game class

Classes

main.py -> entry point of the whole application
1. Player (parent)
    a. AI or Computer (child)
    b. Human (child)
2. Game ""