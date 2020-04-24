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


testGrid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]


print(checkSquare(testGrid, [3, 8], 1))
