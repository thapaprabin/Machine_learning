def print_board(board):
    for i in range(0,9,4):#range(start,stop,skip
        print(" " + " | ".join(board[i:i+3]))
        if i<6:
            print("---+---+---")
board=[" "]*9
print_board(board)