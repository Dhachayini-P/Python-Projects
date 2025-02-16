# Tic-Tac-Toe Game

# Function to display the current board
def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---------")
    print("\n")

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in range(3):
        if all([cell == player for cell in board[row]]):  # Check row
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):  # Check column
            return True

    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True

    if all([board[i][2-i] == player for i in range(3)]):  # Check reverse diagonal
        return True

    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Main game function
def tic_tac_toe():
    # Initial empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Choose who goes first
    player_turn = 'X'

    while True:
        print_board(board)

        # Get the player's move
        print(f"Player {player_turn}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
            if row not in range(3) or col not in range(3):
                print("Invalid position! Please enter row and column between 0 and 2.")
                continue
            if board[row][col] != ' ':
                print("This cell is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter two numbers.")
            continue

        # Make the move
        board[row][col] = player_turn

        # Check if the current player wins
        if check_winner(board, player_turn):
            print_board(board)
            print(f"Player {player_turn} wins!")
            break

        # Check if the board is full (draw)
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player_turn = 'O' if player_turn == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
