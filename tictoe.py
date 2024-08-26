import heapq

class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(state, player):
    max_player = 'X'
    other_player = 'O' if player == 'X' else 'X'

    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -float('inf')}
    else:
        best = {'position': None, 'score': float('inf')}

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, other_player)

        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best

def a_star_search(board, letter):
    empty_squares = board.available_moves()
    best_move = None
    best_score = -float('inf') if letter == 'X' else float('inf')

    for move in empty_squares:
        board.make_move(move, letter)
        score = minimax(board, 'O' if letter == 'X' else 'X')['score']
        board.board[move] = ' '
        board.current_winner = None

        if letter == 'X':
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_move

def play(game, x_player, o_player):
    game.print_board()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player(game)
        else:
            square = x_player(game)

        if game.make_move(square, letter):
            print(f'{letter} makes a move to square {square}')
            game.print_board()
            print('')

            if game.current_winner:
                print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        else:
            print('Invalid move. Try again.')

    print('It\'s a tie!')

def human_move(game):
    valid_square = False
    val = None
    while not valid_square:
        square = input('Enter your move (0-8): ')
        try:
            val = int(square)
            if val not in game.available_moves():
                raise ValueError
            valid_square = True
        except ValueError:
            print('Invalid move. Try again.')
    return val

def ai_move(game):
    return a_star_search(game, 'O')

if __name__ == '_main_':
    t = TicTacToe()
    play(t, human_move,ai_move)
