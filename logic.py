def makeEmptyBoard():
    board = [[0] * 9] * 9
    return board


def printBoard(board):
    for row in board:
        print(row)


def findEmptySpot(board, loc):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                loc[0] = row
                loc[1] = col
                return True
    return False


testGrid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
