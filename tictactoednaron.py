board =     ['','','',
             '','','',
             '','','']

def show_board():
    for i in range (0,9,3):
        print (board[i:i+3])
show_board()

def winning_condition (player):
    return (
    (board [0] == player and board [1]== player and board [2] == player) or
    (board [3] == player and board [4]== player and board [5] == player) or
    (board [6] == player and board [7] == player and board [8] == player) or
    (board [0] == player and board [3] == player and board [6] == player ) or
    (board [1] == player and board [4] == player and board [7] == player) or
    (board [2] == player and board [5] == player and board [8] == player) or
    (board [0] == player and board [5] == player and board [8]== player) or
    (board [2] == player and board [5] == player and board [6] == player))
    