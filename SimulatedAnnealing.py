import math, time, random


SIZE = 8
TEMPERATURE, ALPHA = 1, 0.99

class Board:

    @staticmethod
    def getBoard():
        return [random.randint(0, SIZE - 1) for i in range(0, SIZE)]
        # board[row] = col
    
    @staticmethod
    def getNeighbour(board):
        neighbour = board.copy()
        i = random.randint(0, SIZE - 1)
        while True:
            j = random.randint(0, SIZE - 1)
            if neighbour[i] != j:
                neighbour[i] = j
                return neighbour
    
    @staticmethod
    def getCost(board):
        threats = 0
        # we know that each row has exactly one queen
        for queen in range(0, SIZE):
            for nextQueen in range(queen + 1, SIZE):
                if board[queen] == board[nextQueen]  or abs(queen - nextQueen) == abs(board[queen] - board[nextQueen]):
                    threats += 1
        
        return threats

    @staticmethod
    def show(board):
        for i in range(SIZE):
            for j in range(SIZE):
                print('0', end = '  ') if board[i] != j else print('1', end = '  ')
            print()
        print('Number of pairs of queens that are attacking each other:   %s\n'     %Board.getCost(board))


def simulatedAnnealing(board):
    currentState = board
    global TEMPERATURE
    epsilon = math.e ** (-100)
    while Board.getCost(currentState) != 0 and TEMPERATURE > epsilon:
        TEMPERATURE *= ALPHA
        neighbour = Board.getNeighbour(currentState)
        dE = Board.getCost(neighbour) - Board.getCost(currentState)
        if dE <= 0 or random.uniform(0,1) < math.e ** (-dE / TEMPERATURE):
            currentState = neighbour

    return currentState

if __name__ == '__main__':
    inithialState = Board.getBoard()
    print('\tInitial State:')
    Board.show(inithialState)

    startTime = time.time()
    finalState = simulatedAnnealing(inithialState)
    stopTime = time.time()

    print('\tFinal State:')
    Board.show(finalState)

    print('exec time:    %s  seconds' %(stopTime - startTime))
    