from AI import AI
from Human import Human
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()
    
    def run_game(self):
      print(f"Welcome to the game of RPSLS")
      self.player1.choose_gesture()
      self.player2.choose_gesture()

      self.display_rules()
      self.player1.choose_gesture()
      print(self.player1.chosen_gesture)
      self.display_winner()

    def display_rules(self):
        print("Here are the rules to the game:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard") 
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")