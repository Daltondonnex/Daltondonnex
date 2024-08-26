def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all([spot == player for spot in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([spot in ['X', 'O'] for row in board for spot in row])

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please try again.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] in ['X', 'O']:
                print("This spot is already taken. Please try again.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def main():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    current_player = 'X'

    while True:
        print_board(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        current_player = switch_player(current_player)

if __name__ == "_main_":
    main()
