

import random

def checkWinConditon(player1, player2, score):
    if player1 == player2:
        score.append("draw")
        print("It's a draw!")
        print("-------------------------")
    elif (player1 == "Rock" and player2 == "Scissors"):
        score.append("user")
        print("You played Rock")
        print("You win this round")
        print("-------------------------")
    elif (player1 == "Paper" and player2 == "Rock"):
        score.append("user")
        print("You played Paper")
        print("You win this round")
        print("-------------------------")
    elif (player1 == "Scissors" and player2 == "Paper"):
        score.append("user")
        print("You played Scissors")
        print("You win this round")
        print("-------------------------")
    else:
        score.append("comp")
        print("Computer wins this round")
        print("-------------------------")

def scoreKeeper(score):
    userScore = score.count("user")
    computerScore = score.count("comp")
    draw = score.count("draw")
    if userScore > computerScore:
        print(f"Score: User-{userScore} Computer-{computerScore} Draw-{draw}")
        print("User Wins")
    else:
        print(f"Score: User-{userScore} Computer-{computerScore}")
        print("Computer Wins")


def playGame():
    choices = ["Rock", "Paper", "Scissors"]
    score = []
    for i in range(5):
        computerMove = random.choice(choices)
        userMove = input("Enter your move ")
        if userMove in choices:
            print(f"Computer played {computerMove}")
            checkWinConditon(computerMove,userMove, score)
        else:
            print(f"Invalid input.\nChoose from the following:\n{choices}")
            playGame()
    scoreKeeper(score)

print("Let's play!")
playGame()