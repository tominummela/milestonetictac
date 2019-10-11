#The gameboard

def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])

test_board = ["#","X","O","X","O","X","O","X","O","X"]


def player_input():
    marker = ""
    while marker != "X" or marker != "O":
        marker = input("Please select your marker. X or O, and press ENTER").upper()
    if marker == "X":
        return (X,O)
    else:
        return (O,X)


def place_marker(board,marker,position):
    board[position] = marker


def win_check(board, mark):
    #Horizontal winchecks
    return ((board[7] == mark and board[8] == mark and board[9] or
        board[4] == mark and board[5] == mark and board[6] or
        board[1] == mark and board[2] == mark and board[3] or
    #Vertical winchecks
        board[1] == mark and board[4] == mark and board[7] or
        board[2] == mark and board[5] == mark and board[8] or
        board[3] == mark and board[6] == mark and board[9] or
    #Diagonal winchecks
        board[1] == mark and board[5] == mark and board[9] or
        board[3] == mark and board[5] == mark and board[7] or

