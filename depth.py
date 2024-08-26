import itertools

def check_winner(board):
    for combo in itertools.combinations([0, 1, 2], 3):
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None

def dfs(board, player):
    winner = check_winner(board)
    if winner:
        return 1 if winner == 'X' else -1 if winner == 'O' else 0
    if ' ' not in board:
        return 0

    best_score = float('-inf') if player == 'X' else float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            score = dfs(board, 'O' if player == 'X' else 'X')
            board[i] = ' '
            best_score = max(score, best_score) if player == 'X' else min(score, best_score)
    return best_score

def get_best_move(board):
    best_move = -1
    best_score = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = dfs(board, 'O')
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

board = [' ' for _ in range(9)]

while True:
    print("Current Board:")
    for i in range(3):
        print(board[i * 3:i * 3 + 3])
    print("Enter a number (0-8) to make a move:")
    user_move = int(input())
    if board[user_move] == ' ':
        board[user_move] = 'O'
    else:
        print("Invalid move. Try again.")
        continue

    if check_winner(board):
        print("You win!")
        break

    ai_move = get_best_move(board)
    board[ai_move] = 'X'

    if check_winner(board):
        print("AI wins!")
        break

    if ' ' not in board:
        print("It's a tie!")
        break
