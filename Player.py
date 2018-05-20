import numpy as np

wins = 0        
class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def get_state(self):
        file_name = 'state.json'
        # first run
        if file_name not in os.listdir():
            with open(file_name, 'w') as f:
                json.dump(self.state, f)
        # we have state
        else:
            with open(file_name, 'r') as f:
                self.state = json.load(f)

    def save_state(self):
        file_name = 'state.json'
        self.state['turn'] += 1
        with open(file_name, 'w') as f:
            json.dump(self.state, f)


    def get_alpha_beta_move(self, board):
        utility = evaluation_function(self,board)
        max_value = min(utility)
        max_index = utility.index(max_value)
#        return max_index
        return (evaluation_function(self,board))
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        raise NotImplementedError('Whoops I don\'t know what to do')
   
    def get_expectimax_move(self, board):

        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        raise NotImplementedError('Whoops I don\'t know what to do')


def count_values(self, board, num, player_num):
    numberofwins = 0 
    player_win_str = '{0}' * num 
    player_win_str = player_win_str.format(player_num)
    to_str = lambda a: ''.join(a.astype(str))

    def check_horizontal(b):
        count = 0
        for row in b:
            if player_win_str in to_str(row):
                count += to_str(row).count(player_win_str) 
        return count

    def check_verticle(b):
        return check_horizontal(b.T)

    def check_diagonal(b):
        count = 0 
        for op in [None, np.fliplr]:
            op_board = op(b) if op else b
            root_diag = np.diagonal(op_board, offset=0).astype(np.int)
            if player_win_str in to_str(root_diag):
                count += to_str(root_diag).count(player_win_str) 

            for i in range(1, b.shape[1]-3):
                for offset in [i, -i]:
                    diag = np.diagonal(op_board, offset=offset)
                    diag = to_str(diag.astype(np.int))
                    if player_win_str in diag:
                        count += diag.count(player_win_str) 
        return count 
    numberofwins = check_horizontal(board) + check_verticle(board) + check_diagonal(board) 
    return numberofwins

def min_utility(self, board, col, opponent, player):
    utility = []
    for row in range(5,0,-1):
        if board[row][col] == 0:
            board[row][col] = player
            result = count_values(self, board, 4, player) * 1000
            result += count_values(self, board, 3, player) * 100
            result += count_values(self, board, 2, player) * 10

            result -= count_values(self, board, 3, opponent) * 1000 
            result -= count_values(self, board, 2, opponent) * 10
            utility.append(result)
#                    utility = min_function(self, board)
            board[row][col] = 0

            break
    max_value = min(utility)
    max_index = utility.index(max_value)
    return max_index
            
def evaluation_function(self, board):
    utility = []
    player = self.player_number
    if (player == 1): 
        opponent = 2
    else: 
        opponent = 1
    for col in range (0,7): 
        for row in range(5,0,-1):
            if board[row][col] == 0:
                board[row][col] = player 
                result = count_values(self, board, 4, player) * 1000
                result += count_values(self, board, 3, player) * 100
                result += count_values(self, board, 2, player) * 10

                result -= count_values(self, board, 3, opponent) * 1000 
                result -= count_values(self, board, 2, opponent) * 10
                utility.append(result)
#                    utility = min_function(self, board)
                board[row][col] = 0

                break
    max_value = max(utility)
    max_index = utility.index(max_value)
    return (min_utility(self,board, max_index, player, opponent)) 
#        return (utility)


                
        
    def min_function(self, board):
        utility = []
        opponent = self.player_number
        if (opponent == 1): 
            player = 2
        else: 
            player = 1
        for col in range (0,7): 
            for row in range(5,0,-1):
                if board[row][col] == 0:
                    board[row][col] = player 
                    result = count_values(self, board, 4, player) * 1000
                    result += count_values(self, board, 3, player) * 100
                    result += count_values(self, board, 2, player) * 10

                    result -= count_values(self, board, 3, opponent) * 1000 
                    result -= count_values(self, board, 2, opponent) * 10
                    utility.append(result)
#                    evaluation_function(self, board)
                    board[row][col] = 0
                    break
        return (utility)




class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)





    def get_move(self, board):

        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))
        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move


