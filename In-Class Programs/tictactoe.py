def winner(grid):
    for row in range(3):
        if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2] and grid[row][0] != " ":
            return grid[row][0]
    for col in range(3):
        if grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col] and grid[0][col] != " ":
            return grid[0][col]
    for ldiag in range(3)


def main():
    game1 = [[], [], []]