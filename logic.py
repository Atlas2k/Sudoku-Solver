def makeEmptyBoard():
    board = [[0] * 9] * 9
    return board


def printBoard(board):
    if type(board) == list:
        for row in board:
            print(row)
    else:
        print('This board is unsolvable.')


def findEmptySpot(board):
    loc = [0, 0]
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                loc[0] = row
                loc[1] = col
                return loc, True
    return loc, False


def checkRow(board, loc, n):
    if n in board[loc[0]]:
        return False
    else:
        return True


def checkCol(board, loc, n):
    column = []
    for c in board:
        column.append(c[loc[1]])
    if n in column:
        return False
    else:
        return True


def checkSquare(board, loc, n):
    temp = []
    squares = []
    for y in range(0, 9, 3):
        for x in range(0, 9):
            temp += board[x][y:y+3]
            if len(temp) == 9:
                squares.append(temp)
                temp = []
    if 0 <= loc[1] <= 2:
        if 0 <= loc[0] <= 2:
            if n in squares[0]:
                return False
            else:
                return True
        elif 3 <= loc[0] <= 5:
            if n in squares[1]:
                return False
            else:
                return True
        elif 6 <= loc[0] <= 8:
            if n in squares[2]:
                return False
            else:
                return True
    elif 3 <= loc[1] <= 5:
        if 0 <= loc[0] <= 2:
            if n in squares[3]:
                return False
            else:
                return True
        elif 3 <= loc[0] <= 5:
            if n in squares[4]:
                return False
            else:
                return True
        elif 6 <= loc[0] <= 8:
            if n in squares[5]:
                return False
            else:
                return True
    elif 6 <= loc[1] <= 8:
        if 0 <= loc[0] <= 2:
            if n in squares[6]:
                return False
            else:
                return True
        elif 3 <= loc[0] <= 5:
            if n in squares[7]:
                return False
            else:
                return True
        elif 6 <= loc[0] <= 8:
            if n in squares[8]:
                return False
            else:
                return True


def solveBoard(board):
    loc, Empty = findEmptySpot(board)
    if not Empty:
        return True
    for n in range(1, 10):
        if checkRow(board, loc, n)\
                and checkCol(board, loc, n)\
                and checkSquare(board, loc, n):
            board[loc[0]][loc[1]] = n
            if solveBoard(board):
                return board
            board[loc[0]][loc[1]] = 0
    return False


board1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

board2 = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 0, 0, 9],
          [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0],
          [0, 0, 1, 0, 5, 0, 9, 3, 0],
          [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2],
          [1, 2, 0, 0, 0, 7, 4, 0, 0],
          [0, 4, 9, 2, 0, 6, 0, 0, 7]]


printBoard(solveBoard(board1))
