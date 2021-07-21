from AI import AI
from Human import Human
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()
    
    def run_game(self):
      self.display_welcome()
      self.player1.choose_gesture()
      self.player2.choose_gesture()
      self.display_rules()
      self.player1.choose_gesture()
      print(self.player1.chosen_gesture)
      self.display_winner()

    def display_welcome(self):
     print(f"Welcome to the game of RPSLS")

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
   
    def type_of_player(self):
        player_choice = input("Enter 'single' for single player or 'multi' for multiple players: ")
        if player_choice == 'single':
            print("single player!")
        elif player_choice == 'multi':
            print("multi-player!")
        else:
            print("Please make a selection.")

    def display_winner(self):
        if (self.human.score > self.ai.score):
            print("Human wins!")
        elif (self.human.score < self.ai.score):
            print("AI wins!")
        else:
            print("It's a tie. Play again!")       



    #def best_winner =(Self):
#       player_wins = 0
#       comp_wins = 0
#       play_ties = 0
        
#     while player_wins < play_ties and comp_wins < play_ties:
#             result, user, computer = play()
#   if result == 0:
#       print('Its a tie!! you and the opponent chosen {}. \n'.format(user))
#   elif result == 1:
#       player_wins +=1
#       print('You choosen {} and the opponent chose{}. You are the winner!!: \n'.format(user, computer))
#   else: comp_wins +=1
#       print('You chose {} and the opponent chose {} You LOST!! \n'.format(user, computer))
#   if  player_wins > comp_wins:
#       print('You have won the game! with the best of {}'.format(n))
#   else:
#       print('Oh NO!, the opponent has won with the best of {} Good luck next time!'.format(n))
