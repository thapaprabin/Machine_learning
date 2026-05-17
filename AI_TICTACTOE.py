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

#checks if the required position is empty.If empty puts O,X accordingly.
def make_move(board,position,player):
    if board[position]==" ":
        board[position]=player
        return True
    return False
def human_move(board):
    while True:
        try:
            pos=int(input("Enter position[1-9]"))-1
            if 0<=pos <=8 and board[pos]==" ":
                return pos
            else:
                print("Invalid or occupied")
        except ValueError:
            print("Enter a number.")
def minimax(board,is_maximizing):
    winner=check_winner(board)
    if winner =="O":
        return 10
    elif winner=="X":
        return -10
    elif winner =="tie":
        return 0
    if is_maximizing:
        best_score=-float("inf")
        #loop through all 9 positioin
        for i in range(9):
            if board == " ":
                board[i]="O"
                score=minimax(board,False)
                board[i]=" "
                best_score=max(score,best_score)
        return best_score
    else:
        best_score=float("inf")
        for i in range(9):
            if board[i]==" ":
                board[i]=="X"
                score=minimax(board,True)
                board[i]==" "
                best_score=min(score,best_score)
        return best_score
def ai_move(board):
    best_score=-float("inf")
    best_move=None
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(board,False)
            board[i]=" "
            if score > best_score:
                best_score=score
                best_move=1
    return best_move



    

