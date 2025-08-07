import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check winner
def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if board is full
def is_board_full(board):
    return ' ' not in board

# Minimax function
def minimax(board, depth, is_maximizing):
    if is_winner(board, '😡'):
        return 1
    elif is_winner(board, '😍'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = '😡'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = '😍'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Get best move
def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = '😡'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        while True:
            try:
                user_move = int(input("Enter your move (0-8): "))
                if board[user_move] == ' ':
                    board[user_move] = '😍'
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter number between 0-8.")

        print_board()

        if is_winner(board, '😍'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = '😡'
        print("AI chose:", ai_move)
        print_board()

        if is_winner(board, '😡'):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

# Start the game
play_game()
