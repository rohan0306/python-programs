import random 

def game():
    print("You are playing the game")
    score = random.randint(1,62)

    with open("poem.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score : {score}")
    if (score > hiscore):

        with open("poem.txt", "w") as f:
            f.write(str(score))

    return score
game()