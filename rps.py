import random 

t = ["Rock", "Paper", "Scissors"]

comp = t[random.randint(0,2)]


player = False

while player==False:
    player = input("Rock, Paper, Scissors?")
    if comp == player:
        print("Tie!")

    elif player== "Paper":
        if comp == "Rock":
            print("You Win!,")
        else:
            print("You Lost!")
    elif player=="Rock":
        if comp=="Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose!")
        else:
            print("You win!")
    
    else:
        print("Invalid input")

    player = False
    comp = t[random.randint(0,2)]