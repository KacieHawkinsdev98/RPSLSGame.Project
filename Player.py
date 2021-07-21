import random

 
 
class Player:
  def __init__(self,name):
        self.name = name
        self.gestures_list = ["rock","paper","scissor","lizard","spock"]
        self.score = 0
        self.chosen_gesture = None


  def choose_gesture(self):
     gesture_choice = input("choose a gesture: (rock[1], paper[2], scissors[3],lizard[4],spock[5]): ")
     if gesture_choice == "1": 
       print("you have chosen rock")
     elif gesture_choice == "2":
       print("you have chosen paper")
     elif gesture_choice == "3":
       print("you have chosen scissor")
     elif gesture_choice == "4":
       print ("you have chosen lizard")
     elif gesture_choice == "5":
      print("you have chosen spock")
     return gesture_choice




