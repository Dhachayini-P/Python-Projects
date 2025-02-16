# Connect Four Game in Python

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_1 = "X"
PLAYER_2 = "O"
EMPTY = " "

print("WELCOME TO CONNECT-FOUR GAME👾")
print("*"*30)

# Function to initialize the game board
def create_board():
    return [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

# Function to print the current game board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * (COLUMN_COUNT * 4 - 1))

# Function to check if a column is valid for the next move
def is_valid_column(board, col):
    return board[0][col] == EMPTY

# Function to get the next available row in a given column
def get_available_row(board, col):
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1

# Function to drop a player's piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check for a win condition
def check_win(board, piece):
    # Horizontal check
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True
    
    # Vertical check
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if all(board[row + i][col] == piece for i in range(4)):
                return True
    
    # Diagonal check (positive slope)
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True
    
    # Diagonal check (negative slope)
    for row in range(3, ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False

# Function to play the game
def play_game():
    board = create_board()
    turn = 0  # 0 for Player 1 (X), 1 for Player 2 (O)
    
    while True:
        print_board(board)
        
        # Current player (X or O)
        current_player = PLAYER_1 if turn % 2 == 0 else PLAYER_2
        print(f"Player {current_player}'s turn")
        
        # Get column input from the player
        try:
            col = int(input(f"Choose a column (0-{COLUMN_COUNT - 1}): "))
            if col < 0 or col >= COLUMN_COUNT or not is_valid_column(board, col):
                print("Invalid column. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid column number.")
            continue

        # Get the next available row in the chosen column
        row = get_available_row(board, col)
        drop_piece(board, row, col, current_player)
        
        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw (board full)
        if all(board[0][col] != EMPTY for col in range(COLUMN_COUNT)):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch turn
        turn += 1

# Start the game
if __name__ == "__main__":
    play_game()
