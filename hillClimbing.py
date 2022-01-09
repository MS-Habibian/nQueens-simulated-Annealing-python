import random

SIZE = 8

class Board:
    @staticmethod
    def get_random_board():
        """
        return a board with one queen per row
        example: [1, 2, 4, 6, 3, 2,  2, 1] => board[row] = column
        """
        return [random.randint(0, SIZE - 1) for i in range(0, SIZE)]
    
    @staticmethod
    def get_random_neighbour(board):
        neighbour = board.copy()
        # select random row
        i = random.randint(0, SIZE - 1)
        # select random column
        while True:
            j = random.randint(0, SIZE - 1)
            # don't return the same board as neighbour
            if neighbour[i] != j:
                neighbour[i] = j
                return neighbour

    @staticmethod
    def get_best_neighbour(board):
        """
        scan all neighbours of board and return the best(less threats)
        """
        best_neighbour = []
        best_neighbour_threats = 0
        for row in range(0, SIZE):
            for col in range(0, SIZE):
                if board[row] == col:
                    continue # neighbour should not be equal with initial board
                neighbour = board.copy()
                neighbour[row] = col
                neighbour_threats = Board.get_cost(neighbour)
                if not best_neighbour or  neighbour_threats < best_neighbour_threats:
                    best_neighbour = neighbour
                    best_neighbour_threats = neighbour_threats
        return best_neighbour # , best_neighbour_threats
                


    @staticmethod
    def get_cost(board):
        """
        return the number of pairs of queens which can attack each other
        """
        threats = 0
        # we know that each row has exactly one queen
        for queen in range(0, SIZE):
            for nextQueen in range(queen + 1, SIZE):
                if board[queen] == board[nextQueen]  or abs(queen - nextQueen) == abs(board[queen] - board[nextQueen]):
                    threats += 1
        
        return threats

    @staticmethod
    def print_board(board):
        for i in range(SIZE):
            for j in range(SIZE):
                print('0', end = '  ') if board[i] != j else print('1', end = '  ')
            print()
        print('Number of pairs of queens which can each other:   %s\n'  %Board.get_cost(board))

def hill_climbing(board):
    while True:
        current_cost = Board.get_cost(board)
        if current_cost == 0:
            # optimal minimum (answer)
            return board
        neighbour = Board.get_best_neighbour(board)
        neighbour_cost = Board.get_cost(neighbour)
        if neighbour_cost < current_cost:
            print("going to best neighbour...")
            board = neighbour
        elif neighbour_cost == current_cost: # shoulder...
            # we are on a shoulder 
            # go to a random neighbour
            print('SHOULDER: going to ranodm neighbour...')
            board = Board.get_random_neighbour(board)
        else:
            # on local optimum
            print('LOCAL OPTIMUM: restarting with random board...')
            board = Board.get_random_board()
            Board.print_board(board)


if __name__ == '__main__':
    initial_board = Board.get_random_board()
    print('Initial state:')
    Board.print_board(initial_board)
    final_state = hill_climbing(initial_board) # better to call with b.copy()
    print('Final state:')
    Board.print_board(final_state)
