board= [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def display_board():
    print("|".join(board[0:3]))
    print("- - - ")
    print("|".join(board[3:6]))
    print("- - - ")
    print("|".join(board[6:]))


turn = "X"
while True:
    display_board()
    ask = int(input("Where do you want to put it?: "))
    if board[ask] == " ":
        board[ask] = turn

    if board[0]==board[1]==board[2] and board[0]!= " ":
        print(turn, ("wins"))
        break
    elif board[3]==board[4]==board[5] and board[3]!= " ":
        print(turn, ("wins"))
        break
    elif board[6]==board[7]==board[8] and board[6]!= " ":
        print(turn, ("wins"))
        break
    elif board[0]==board[3]==board[6] and board[0]!= " ":
        print(turn, ("wins"))
        break
    elif board[1]==board[4]==board[7] and board[1]!= " ":
        print(turn, ("wins"))
        break
    elif board[2]==board[5]==board[8] and board[2]!= " ":
        print(turn, ("wins"))
        break
    elif board[0]==board[4]==board[8] and board[0]!= " ":
        print(turn, ("wins"))
        break
    elif board[2]==board[4]==board[6] and board[6]!= " ":
        print(turn, ("wins"))
        break
    elif " " not in board:
        print("It is a tie")
    
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    
    



