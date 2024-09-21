import random

def game():
    print("You are playing game -> ")
    score = random.randint(1,50)

    with open("Hi_score.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0

    print("Your score : ",score)
    if score > highscore:
        with open("Hi_score.txt","w") as f:
            f.write(str(score))

    return score

game()