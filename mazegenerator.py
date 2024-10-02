# Define a simple maze: 1 is a wall, 0 is a path
maze1 = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0]
]

# Player starts at the top-left corner
player_row = 0
player_col = 0

# Function to print the maze with the player's position
def print_maze():
    for row in range(len(maze1)):  # Loop through each row
        for col in range(len(maze1[row])):  # Loop through each column
            if row == player_row and col == player_col:
                print("P", end=" ")  # Print the player
            elif maze1[row][col] == 1:
                print("█", end=" ")  # Print a wall
            else:
                print(" ", end=" ")  # Print a path
        print()  # Move to the next row

# Function to move the player
def move_player():
    global player_row, player_col
    move = input("Move (W = Up, A = Left, S = Down, D = Right): ").upper()
    
    # Calculate new position based on input
    new_row = player_row
    new_col = player_col

    if move == 'W':  # Move up
        new_row -= 1
    elif move == 'S':  # Move down
        new_row += 1
    elif move == 'A':  # Move left
        new_col -= 1
    elif move == 'D':  # Move right
        new_col += 1

    # Check if the new position is valid (within bounds and on a path)
    if 0 <= new_row < len(maze1) and 0 <= new_col < len(maze1[0]) and maze1[new_row][new_col] == 0:
        player_row = new_row
        player_col = new_col
    else:
        print("Blocked! You can't move there.")

# Main game loop
while (player_row, player_col) != (4, 4):  # The exit is at (4, 4)
    print_maze()  # Show the maze with the player's position
    move_player()  # Ask the player for their next move

print("Congratulations! You reached the exit!")
