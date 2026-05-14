def print_board(board):
    for i in range(0,9,3):#range(start,stop,skip
        print(" " + " | ".join(board[i:i+3]))
        if i<4:
            print("---+---+---")
board=["X"]*9
print_board(board)

