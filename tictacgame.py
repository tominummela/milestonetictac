#The gameboard

def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])

test_board = ["#","X","O","X","O","X","O","X","O","X"]
display_board(test_board)

def player_input():
    marker = ""
    while marker != "X" or marker != "O":
        marker = input("Please select your marker. X or O, and press ENTER").upper()
    if marker == "X":
        return (X,O)
    else:
        return (O,X)

player_input()

def board_marker():
    