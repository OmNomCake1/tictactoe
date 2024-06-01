# A simple 2 player tic tac toe game
# made by Ryan Wong

rows = 3
columns = 3

# IDK classes yet
player_1 = {
    "name": "",
    "player_type": "",
    "num_wins": 0
}

player_2 = {
    "name": "",
    "player_type": "",
    "num_wins": 0
}

# Print gameboard function
def print_gameboard():
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])

# Int checker function
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Gameboard full function
def is_full(board):
    for row in board:
        if "-" in row:
            return False
    return True

# Check winner function
# Input: game_board rows x columns 2d array
# Outputs: True or False
def winner(board):
    # Check if any rows are all equal
    for row in range(rows):
        # This uses a "Generator expression" and "List Comprehension" to check if all values in array are equal
        # <expression for i in array/range if expression> (gives an iterable of a set of expressions)
        # can be put in [] to make a new array from this, or () to make a generator (stream)

        # This is actually very similar to .steam().filter().map().collect() etc. in java/JS etc. 
        # The first expression is the map(), for i in array is the .stream() and the if expression is .filter()
        # this by itself streams the mapped data and you can list() it to create an array
        if all(board[row][col] == board[row][0] for col in range(columns)):
            if board[row][0] == "-":
                continue
            return True
    
    # Check if any columns are all equal
    for col in range(columns):
        if all(board[row][col] == board[0][col] for row in range(rows)):
            if board[0][col] == "-":
                continue
            return True
    
    # Check if forward diagonal is equal
    if all(board[i][i] == board[0][0] for i in range(rows)) and board[0][0] != "-":
        return True
    
    # check if reverse diagonal is equal]
    if all(board[rows - 1 - i][i] == board[0][2] for i in range(rows)) and board[0][2] != "-": 
        return True
    
    return False

# Game setup 
# set up a row x column 2d matrix
game_board = [["-" for col in range(columns)] for row in range(rows)]



#############################################################################################


player_1["name"] = input("Hello! Please enter Player 1's name:\n")
player_1["player_type"] = input("Enter Player 1's type 'X' or 'O' ('X' goes first)\n").upper()

while player_1["player_type"] not in ("X", "O"):
    player_1["player_type"] = input("Please enter X or O\n")


player_2["name"] = input("Please enter Player 2's name:\n")

if player_1["player_type"] == "X":
    current_player = player_1
    player_2["player_type"] = "O"
else:
    current_player = player_2
    player_2["player_type"] = "X"

row = 0
col = 0

print_gameboard()


while is_full(game_board) == False:
    print(f"{current_player["name"]}'s turn!")
    
    # Get row and col value while error checking:
    # 1. Not a number
    # 2. Out of bounds (0 < x < rows/columns)
    # 3. value in game_board is not already taken ("O" or "X")

    while True:
        row = input("Input row value: ")
        col = input("Input col value: ")

        if is_integer(row) == False or is_integer(col) == False: 
            print("Please enter a digit")
            continue
        elif int(row) < 0 or int(row) > rows - 1:
            print(f"Please enter a row between 0 and {rows - 1}")
            continue
        elif int(col) < 0 or int(col) > columns - 1:
            print(f"Please enter a col between 0 and {columns - 1}")
            continue
        elif game_board[int(row)][int(col)] in ("X", "O"):
            print("Square already taken!")
            continue
        else:
            # convert strings to int
            row = int(row)
            col = int(col)
            break
        
    game_board[row][col] = current_player["player_type"]
    print_gameboard()


    # Now we need to check if anyone wins
    if winner(game_board) == True:
        print(f"The winner is {current_player["name"]}! Congratulations")
        break

    # Change current player
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1

if is_full(game_board) and winner(game_board) == False:
    print("It's a draw!")