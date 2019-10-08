board = ["___|___|___","___|___|___","   |   |   "]

boarddict = {"pos1":"board[2][23]","pos2":"board[2][27]","pos3":"board[2][31]",
             "pos4":"board[1][12]","pos5":"board[1][16]","pos6":"board[1][20]",
             "pos7":"board[0][1]","Pos8":"board[0][5]","pos9":"board[0][9]"}

def playboard():
    #This prints the empty board
    print(board[0])
    print(board[1])
    print(board[2])

print(playboard())

def players():
    playerlist[playerx, playero]
    player = input("Type Y if you want to play as x and go first, type N if you want to play as o, go second and lose")
    if player input == str("Y"):
        player = playerx
    elif player input == str("N"):
        player = playero
    else:
        print("You need to learn to either read or type, try again.")

def playerinputs():
    #fill the board as game progresses
    # check for 3 in a row
    #check for full board
    #check for replay willingness









#_7_|_8_|_9_
#_4_|_5_|_6_
# 1 | 2 | 3