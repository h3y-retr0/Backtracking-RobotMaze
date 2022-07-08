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

