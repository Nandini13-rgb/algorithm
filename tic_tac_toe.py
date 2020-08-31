board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


winner = None
current_player = "x"


def display(board):
    print(board[0] + "-" + board[1] + "-" + board[2])
    print(board[3] + "-" + board[4] + "-" + board[5])
    print(board[6] + "-" + board[7] + "-" + board[8])


def instructions(board):
    display(board)
    print(current_player + "'s turn")
    position = int(input("enter the position where you want to play")) - 1
    board[position] = current_player
    flip_player()
    return board


def check_game(board):
    global winner
    # row check
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    if board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    if board[6] == board[7] == board[8]:
        winner = board[6]
        return True
    # column check
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    if board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    if board[2] == board[5] == board[8]:
        winner = board[2]
        return True
    # diagonal check
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    if board[2] == board[4] == board[6]:
        winner = board[2]
        return True
    return False


def flip_player():
    global current_player
    if current_player == "x":
        current_player = "0"
    elif current_player == "0":
        current_player = "x"
    return current_player


def play():
    player = None
    count = 0
    while not check_game(board):
        instructions(board)
        count += 1
        if count == 9:
            print("This is a tie between both players")
            return
        display(board)

    if winner == "0":
        print("winner is 0")
    elif winner == "x":
        print("winner is x")
    else:
        print("There is a tie")
play()
