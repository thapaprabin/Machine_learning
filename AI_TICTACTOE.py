def print_board(board):
    for i in range(0,9,3):#range(start,stop,skip
        print(" " + " | ".join(board[i:i+3]))
        if i<4:
            print("---+---+---")
board=["X"]*9
print_board(board)

#to check winner 
def check_winner(board):
    lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8)]#2diagonals 3horizontal and 3 vertical
    #all the possible winning lines
    for a,b,c in lines:
        if board[a]==board[b]==board[c] and board[a] != "":
            return board[a]
    if " " not in board:
        return "tie"
    return None
