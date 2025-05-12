import random

def drawBoard(board,ref):
    print(f" {board[0]} | {board[1]} | {board[2]}     {ref[0]} | {ref[1]} | {ref[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}     {ref[3]} | {ref[4]} | {ref[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}     {ref[6]} | {ref[7]} | {ref[8]} ")

def checkWinCondition(board, player):
    winConditions = [[0,1,2], [3,4,5], [6,7,8],  # rows
                    [0,3,6], [1,4,7], [2,5,8],  # columns
                    [0,4,8], [2,4,6]]           # diagonals
    
    for condition in winConditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def playerMove(board, emptyCells, player):
    while True:
        try:
            print(f"Available options: {emptyCells}")
            userMove = int(input(f"Choose the square for your move (0-8): "))
            if userMove in emptyCells:
                board[userMove] = player
                emptyCells.remove(userMove)
                return
            else:
                print("That square is not available. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def computerMove(board, emptyCells, computer):
    compMove = random.choice(emptyCells)
    print(f"Computer's move: {compMove}")
    board[compMove] = computer
    emptyCells.remove(compMove)

def playGame():
    board = [" " for x in range(9)]
    reference = [x for x in range(9)]
    emptyCells = list(range(9))
    
    # Choose X or O
    while True:
        character = input("Do you want to be X or O? ").upper()
        if character in ["X", "O"]:
            player = character
            computer = "O" if player == "X" else "X"
            break
        else:
            print("Please choose either X or O.")
    
    # Coin toss to decide who goes first
    coinFaces = ["head", "tails"]
    coinToss = random.choice(coinFaces)
    userChoice = input("Choose either head or tails: ").lower()
    print(f"\nCoin toss result: {coinToss}")
    
    if coinToss == userChoice:
        current_player = player
        print("You go first!")
    else:
        current_player = computer
        print("Computer goes first!")
        
    while True:
        drawBoard(board, reference)
        
        if current_player == player:
            playerMove(board, emptyCells, player)
            if checkWinCondition(board, player):
                drawBoard(board, reference)
                print("Congratulations! You win!")
                break
        else:
            computerMove(board, emptyCells, computer)
            if checkWinCondition(board, computer):
                drawBoard(board, reference)
                print("Computer wins!")
                break
        
        if not emptyCells:
            drawBoard(board, reference)
            print("It's a draw!")
            break
        
        # Switch players
        if current_player == player:
            current_player = computer
        else:
            current_player = player

playGame()