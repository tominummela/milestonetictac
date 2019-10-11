#The gameboard

def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])

test_board = ["#","X","O","X","O","X","O","X","O","X"]
tut_board = ["#","1","2","3","4","5","6","7","8","9"]

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
    return ((board[7] == mark and board[8] == mark and board[9]) or
            (board[4] == mark and board[5] == mark and board[6]) or
            (board[1] == mark and board[2] == mark and board[3]) or
    #Vertical winchecks
            (board[1] == mark and board[4] == mark and board[7]) or
            (board[2] == mark and board[5] == mark and board[8]) or
            (board[3] == mark and board[6] == mark and board[9]) or
    #Diagonal winchecks
            (board[1] == mark and board[5] == mark and board[9]) or
            (board[3] == mark and board[5] == mark and board[7]))

import random
def choose_first():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):
    return board[position] == " "

def board_full_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose your next move: 1-9"))
    return position

def replay():
        return input("Do you want to play again? YES or NO").lower().startswith("y")


#-----------------------------------------------------------------------------
#---------------------------------THE GAME------------------------------------
#-----------------------------------------------------------------------------

print("Welcome to Tic Tac Toe!")
print("The boards layout is like a numpad:")
(display_board(tut_board))

# Reset board to all empty

#Ask who goes first or random

# Start the game, check for win condition and full board with while

#Alternate turns between p1 and p2 (X and O)

#Congratulate winner and ask for replay
