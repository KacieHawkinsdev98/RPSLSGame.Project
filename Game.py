import random
from AI import AI
from Human import Human
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()
    
    
    def display_welcome(self):
     print(f"Welcome to the game of RPSLS")

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.single_or_multiplayer()


    
    def display_rules(self):
     rules = """Here are the rules to the game:,
    Rock crushes Scissors,
         Scissors cuts Paper,
         Paper covers Rock,
         Rock crushes Lizard,
         Lizard poisons Spock,
         Spock smashes Scissors,
         Scissors decapitates Lizard, 
         Lizard eats Paper,
         Paper disproves Spock,
         Spock vaporizes Rock"""
     print(rules)
 
    def single_or_multiplayer(self):
     player_choice = input("choose _single or _multiplayer:")
     if player_choice == "single":
        self.player1.choose_gesture()
        self.player2.choose_gesture()
        
     elif player_choice == "multiplayer":
      self.player1.choose_gesture()
      self.player1.choose_gesture()
    
         
    
         
    
         


