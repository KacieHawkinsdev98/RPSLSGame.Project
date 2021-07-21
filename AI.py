import random
from Player import Player

class AI(Player):
    def __init__(self):
        super().__init__(self)
    pass

def choose_gesture(self):
     self.chosen_gesture = random.choice(self.gestures_list)
     if self.chosen_gesture == "rock":
      print("cpu has chosen rock")
     elif self.chosen_gesture == "paper":
      print("cpu has chosen paper")
     elif self.chosen_gesture == "scissor":
      print("cpu has chosen scissor")
     if self.chosen_gesture == "lizard":
      print("cpu has chosen lizard")
     if self.chosen_gesture == "spock":
      print("cpu has chosen spock")
      return self.chosen_gesture