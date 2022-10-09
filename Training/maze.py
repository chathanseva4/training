# find empty 
from curses import flash
from operator import truediv


def  find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                return (i,j)

def valid(board,num,i,j):
    # check rows
    for k in range(len(board[0])):
        if board[i][k]==num and j!=k:
            return False
    # checking cols
    for k in range(len(board)):
        if board[k][j]==num and k!=i:
            return False
    # checking the grid 
    grid_x=j//3
    grid_y=i//3
    for k in range(grid_y*3,(grid_y*3)+3):
        for s in range(grid_x*3,(grid_x*3)+3):
            if board[k][s]==num and k!=i and s!=j:
                return False
    return True



def solve(board):
    i,j=find_empty(board)
    if i==None and j==None:
        return True
    for attempt in range(1,10):
        if(valid(board,attempt,i,j)):
            board[i][j]=attempt
            if solve(board):
                return True
            board[i][j]
    return False


sudoku_board=[
    [7,0,0,0,0,9,3,0,1],
    [1,0,0,0,2,0,0,0,0],
    [3,0,0,0,8,0,0,0,6],
    [6,0,0,7,0,0,0,0,5],
    [0,8,0,0,9,0,0,0,3],
    [0,0,0,0,0,0,0,0,0],
    [0,4,0,0,5,0,0,0,9],
    [0,6,0,0,0,2,0,5,0],
    [0,0,0,0,0,0,2,1,0]
]


solve(sudoku_board)

