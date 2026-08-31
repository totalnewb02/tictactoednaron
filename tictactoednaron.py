board =     ['','','',
             '','','',
             '','','']

def show_board():
    for i in range (0,9,3):
        print (board[i:i+3])
show_board()