import heapq

class Node:
    def _init_(self, board, player, parent=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

    def _lt_(self, other):
        return self.f < other.f

# Function to check the winner of the game
def check_winner(board):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    for condition in win_conditions:
        if condition[0] == condition[1] == condition[2] and condition[0] != ' ':
            return condition[0]
    return None

# Function to print the board
def print_board(board):
    for i in range(3):
        print(board[3*i] + '|' + board[3*i+1] + '|' + board[3*i+2])
        if i < 2:
            print('-----')

# Heuristic function to evaluate the board
def heuristic(board, player):
    if check_winner(board) == player:
        return 1
    elif check_winner(board) == ('O' if player == 'X' else 'X'):
        return -1
    return 0

# Function to generate the next possible states
def generate_next_states(board, player):
    next_states = []
    for i in range(9):
        if board[i] == ' ':
            new_board = board[:]
            new_board[i] = player
            next_states.append(new_board)
    return next_states

# Function to implement A* search for Tic-Tac-Toe
def a_star_tictactoe():
    initial_board = [' ' for _ in range(9)]
    initial_node = Node(initial_board, 'X')
    open_set = []
    heapq.heappush(open_set, initial_node)
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        current_board = current_node.board
        print_board(current_board)
        print()

        winner = check_winner(current_board)
        if winner:
            print(f"Winner is: {winner}")
            return

        if ' ' not in current_board:
            print("It's a draw!")
            return

        closed_set.add(tuple(current_board))
        next_player = 'O' if current_node.player == 'X' else 'X'
        next_states = generate_next_states(current_board, current_node.player)

        for state in next_states:
            if tuple(state) in closed_set:
                continue

            next_node = Node(state, next_player, current_node)
            next_node.g = current_node.g + 1
            next_node.h = heuristic(state, current_node.player)
            next_node.f = next_node.g + next_node.h

            heapq.heappush(open_set, next_node)

a_star_tictactoe()
