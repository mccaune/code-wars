"""
Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
Examples

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
"""

def valid_solution(board):
    count_row = 0
    count_column = 0
    count_sub = 0

    #print('\n','rinda:', '\n')
#rindas analīze, pārbaudam vai rinda sastāv no 9 skaitļiem, kas neatkārtojas
    for row in board:
        row_lst = []
        for row_number in row:
            if row_number not in row_lst:
                row_lst.append(row_number)
                if len(row_lst) == 9 :
                    count_row += 1
                    #print('rinda neatkartojas', row_lst)
        

    #print('\n','kolona:', '\n')
#kolonas analīze, pārbaudam vai katras rindas n-tais elements izveido sarakstu ar 9 vienībām
    for i in range(9):
        column_lst = []
        for row in board:
            if row[i] not in column_lst:
                column_lst.append(row[i])
                if len(column_lst) == 9:
                    count_column += 1
                    #print('kolona neatkartojas', column_lst)
        
        

    #print('\n','sub-grid:', '\n')
# sub-grid analīze, pārbaudam vai katrs 3x3 sub grids sastāv no 9 dažādiem skaitļiem
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            sub_lst = []
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] not in sub_lst:
                        sub_lst.append(board[r][c])
                        if len(sub_lst) == 9:
                            count_sub += 1
                            #print('sub-grid neatkartojas', temp)
    
    
    

        
    print('count_row ', count_row)
    print('count_column ', count_column)
    print('count_sub ', count_sub)

    if count_column == 9 and count_row == 9 and count_sub == 9:
        return True
    else:
        return False

