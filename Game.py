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