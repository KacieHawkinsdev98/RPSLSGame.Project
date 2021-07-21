from AI import AI
from Human import Human
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()
    
