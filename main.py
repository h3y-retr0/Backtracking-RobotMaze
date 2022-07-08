maze = [[".", ".", ".", "."],
        [".", "x", "x", "x"],
        [".", ".", ".", "x"],
        ["x", "x", ".", "."]]

def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)
    

def helper(maze, sol, pos_row, pos_col):
    num_row = len(maze)
    num_col = len(maze[0])

    # BASE CASES

    if pos_row == num_row - 1 and pos_col == num_col - 1:
        # Alredy Home
        return sol
    elif pos_row >= num_row or pos_col >= num_col:
        # Out of bounds
        return None
    if maze[pos_row][pos_col] == 'x':
        # You have hit an obstacle
        return None
    

    # RECURSIVE CASES

    # Try right
    
    sol.append("r")
    sol_right = helper(maze, sol, pos_row, pos_col + 1)
    if sol_right is not None:
        # You've reached a solution
        return sol_right
    

    # Backtrack
    sol.pop()

    # Try down
    sol.append("d")
    sol_down = helper(maze, sol, pos_row + 1, pos_col)
    if sol_down is not None:
        return sol_down
    
    #No sol
    sol.pop()
    return None

print_maze(maze)

check = input('Type "y" if you want to solve this problem:  ')

if check == "y" or check == "Y":
    solve_maze(maze)
else:
    exit