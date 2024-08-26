def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    while not check_winner(board, "X") and not check_winner(board, "O") and not is_full(board):
        x, y = map(int, input("Enter the position to place 'X' (e.g., 0 1): ").split())
        if board[x][y] == " ":
            board[x][y] = "X"
            print_board(board)
            if check_winner(board, "X"):
                print("You win!")
                break
            if is_full(board):
                print("It's a tie!")
                break
            move = get_best_move(board)
            board[move[0]][move[1]] = "O"
            print("Computer's move:")
            print_board(board)
            if check_winner(board, "O"):
                print("Computer wins!")
                break

play_game()
