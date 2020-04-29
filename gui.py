from logic import board1, solveBoard
import tkinter as tk


def play():
    def solve():
        board = solveBoard(board1)
        if type(board) == list:
            for i in range(0, 9):
                solvedBoard.insert(i, board[i])
        else:
            for i in range(0, 9):
                solvedBoard.insert(i, '')
            solvedBoard.insert(0, ' Solved/No Sol!')

    root = tk.Tk()

    unsolvedBoard = tk.Listbox(root, highlightbackground='#313847',
                               selectmode='extended', bg='#313847', height=9,
                               width=13, fg='#D7DEEA', font=('Helvatica', 32))
    for i in range(0, 9):
        unsolvedBoard.insert(i, board1[i])
    unsolvedBoard.grid(row=0, column=0)

    solvedBoard = tk.Listbox(root, highlightbackground='#313847',
                             selectmode='extended', bg='#313847', height=9,
                             width=13, fg='#D7DEEA', font=('Helvatica', 32))
    solvedBoard.grid(row=0, column=2)

    button = tk.Button(root, text='Solve Board!', fg='#D7DEEA',
                       bg='#4A566C', command=solve)
    button.grid(row=0, column=1, sticky='s')

    root.configure(bg='#313847')
    root.title('Amer\'s Basic Sudoku')
    root.mainloop()
