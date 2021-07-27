from random import choice, randint
print("Rock...")
print("Paper...")
print("Scissor...")


#player1 = input("Player1 enter your move: ")
player1 = choice(["rock", "paper", "scissor"])
# for i in range(0, 10):
#     print("****No Cheating****\n")
player2 = input("Player2 enter your move: ")

if player1 == player2:
    print("Game Tie!!!")
elif player1 == "rock" and player2 == "scissor":
    print("Player1 win!!!")
elif player1 == "rock" and player2 == "paper":
    print("Player2 wins!!")
elif player1 == "paper" and player2 == "rock":
    print("Player1 win!!!")
elif player1 == "paper" and player2 == "scissor":
    print("Player2 wins!!")
elif player1 == "scissor" and player2 == "rock":
    print("Player2 wins!!")
elif player1 == "scissor" and player2 == "paper":
    print("Player1 wins!!")
else:
    print("Something went wrong!!!")
    
print("player1 move: "+player1)