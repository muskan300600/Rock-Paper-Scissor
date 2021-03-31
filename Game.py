import random


def Game(a, b):
    if a == b:
        return None
    elif a == 'r':
        if b == 'p':
            return True
        elif b == 's':
            return False
    elif a == 'p':
        if b == 'r':
            return False
        elif b == 's':
            return True
    elif a == 's':
        if b == 'p':
            return False
        elif b == 'r':
            return True

option = input("Multiplayer (M) or Single Player(S)?")
if option == 'S':
   print("System's Turn: Rock(r), Paper(p) or Scissor(s)?") #name prompt
   randNo = random.randint(1,3) #chose a random number number among 1,2 and 3
   if randNo == 1:
     system = 'r'
   elif randNo == 2:
     system = 'p'
   elif randNo == 3:
     system = 's'

   you = input("Player 1: Rock(r), Paper(p) or Scissor(s)?")
   play1 = Game(system , you) #calling the method

   print(f"System chose {system}")
   print(f"You chose {you}")


   if play1 == None:
    print("This game is a Tie")
   elif play1 == True:
    print("You win")
   elif play1 == False:
    print("You lose")

elif option == 'M':
      player1 = input("Player 1: Rock(r), Paper(p) or Scissor(s)?")
      player2 = input("Player 1: Rock(r), Paper(p) or Scissor(s)?")

      play2 = Game(player1 , player2)

      print(f"System chose {player1}")
      print(f"You chose {player2}")

      if play2 == None:
          print("This game is a Tie")
      elif play2 == True:
          print("You win")
      elif play2 == False:
          print("You lose")






