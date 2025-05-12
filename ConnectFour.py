def create_board():
    board = []
    for _ in range(6):  # 6 rows
        row = []
        for _ in range(7):  # 7 columns
            row.append(' ')
        board.append(row)
    return board
    

def print_board(board):
    # Print column numbers
    print(' '.join(str(i+1) for i in range(7)))
    
    # Print board rows
    for row in board:
        print('|' + '|'.join(row) + '|')
    print('-' * 15)

def is_valid_move(board, column):
    # Check if column is within range and not full
    return 0 <= column < 7 and board[0][column] == ' '

def drop_piece(board, column, player):
    # Piece goes in the lowest empty row
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            return True
    return False

def check_winner(board, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if (board[row][col] == board[row][col+1] == 
                board[row][col+2] == board[row][col+3] == player):
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if (board[row][col] == board[row+1][col] == 
                board[row+2][col] == board[row+3][col] == player):
                return True

    # Check diagonal (right slope)
    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row+1][col+1] == 
                board[row+2][col+2] == board[row+3][col+3] == player):
                return True

    # Check diagonal (left slope)
    for row in range(3, 6):
        for col in range(4):
            if (board[row][col] == board[row-1][col+1] == 
                board[row-2][col+2] == board[row-3][col+3] == player):
                return True

    return False

def is_board_full(board):
    for col in range(7):
        if board[0][col] == ' ':
            return False
    return True

def play_connect_four():
    #Initial board
    board = create_board()
    current_player = 'X'
    game_over = False

    print("Welcome to Connect Four!")
    print("Player X goes first. Players take turns dropping pieces into columns.")

    while not game_over:
        # Print current board state
        print_board(board)
        
        # Get player move
        while True:
            try:
                print(f"Player {current_player}'s turn")
                column = int(input("Choose a column (1-7): ")) - 1
                
                # Validate and execute move
                if is_valid_move(board, column):
                    drop_piece(board, column, current_player)
                    break
                else:
                    print("Invalid move. Try again.")
            
            except ValueError:
                print("Please enter a valid column number.")

        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

play_connect_four()