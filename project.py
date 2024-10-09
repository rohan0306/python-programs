# 1 -  Snake, -1 Water, 0 Gun

import random 
computer = random.choice([-1, 1, 0])
yourstr = input("Enter your choice")
yourdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1 : "Water", 0: "Gun"}

you = yourdict[yourstr]

print(f"Your choice is {reversedict[you]} \n Computer choice is{reversedict[computer]} ")

if computer == you:
    print("Its a draw")

else:
    if (computer == -1 and you == 1):
        print("You win")

    elif (computer == 1 and you == -1):
        print("You loose")

    elif (computer == -1 and you == 0):
        print("You loose")

    elif (computer == 1 and you == 0):
        print("You win")

    elif (computer == 0 and you == -1):
        print("You win")

    elif (computer == 0 and you == 1):
        print("You loose")

    else:
        print("Something went wrong")


