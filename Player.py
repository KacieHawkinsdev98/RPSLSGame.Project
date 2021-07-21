
class player:
 
 
 class Player:
  def __init__(self,name):
        self.name = name
        self.gestures_list = ["rock","paper","scissor","lizard","spock"]
        self.score = 0
        self.chosen_gesture = None




#written code but needs to fix, test, and run. Repeat! 
     # def play():
#     user = input("What is your choice? 'r' = rock, 'p' = paper, or 's' = scissor ???")
#     user = user.lower()

#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return (0, user, computer)

    
#     if the_winner(user, computer):
#         return (1, user, computer)

#     return (-1, user, computer)


#     def the_winner(player, opponent):
#         if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#             return True

#         return False

    
# def best_winner =(n):
#     player_wins = 0
#     comp_wins = 0
#     play_ties = 0
    
#     while player_wins < play_ties and comp_wins < play_ties:
#         result, user, computer = play()
#         if result == 0:
#             print('Its a tie!! you and the opponent chosen {}. \n'.format(user))
#         elif result == 1:
#             player_wins +=1
#             print('You choosen {} and the opponent chose{}. You are the winner!!: \n'.format(user, computer))
#         else: comp_wins +=1
#             print('You chose {} and the opponent chose {} You LOST!! \n'.format(user, computer))
#         if player_wins > comp_wins:
#             print('You have won the game! with the best of {}'.format(n))
#         else:
#             print('Oh NO!, the opponent has won with the best of {} Good luck next time!'.format(n))

#     if __name__ == '__main__':
#         best_winner(3)
