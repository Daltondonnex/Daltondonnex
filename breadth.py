from collections import deque

def check_win(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    for condition in win_conditions:
        if all(cell == player for cell in condition):
            return True
    return False

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def bfs_tic_tac_toe():
    board = [' ' for _ in range(9)]
    queue = deque([(board, 'X')])

    while queue:
        current_board, current_player = queue.popleft()

        if check_win(current_board, 'X'):
            return current_board
        if check_win(current_board, 'O'):
            continue

        empty_cells = [i for i in range(9) if current_board[i] == ' ']
        for i in empty_cells:
            new_board = current_board[:]
            new_board[i] = current_player
            queue.append((new_board, 'X' if current_player == 'O' else 'O'))

def play_game():
    board = [' ' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as 'X'. Enter a number from 0 to 8 to make your move.")
    print_board(board)

    while True:
        user_move = int(input("Enter your move (0-8): "))
        if board[user_move] != ' ':
            print("Invalid move. That spot is already taken. Try again.")
            continue

        board[user_move] = 'X'
        print_board(board)

        if check_win(board, 'X'):
            print("Congratulations! You won!")
            break

        if ' ' not in board:
            print("It's a draw!")
            break

        print("AI is making a move...")
        board = bfs_tic_tac_toe()
        print_board(board)

        if check_win(board, 'O'):
            print("AI wins!")
            break

        if ' ' not in board:
            print("It's a draw!")
            break

play_game()