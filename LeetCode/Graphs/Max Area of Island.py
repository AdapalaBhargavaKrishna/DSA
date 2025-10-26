def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
    
    max_area = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                max_area = max(max_area, dfs(row, col))
    return max_area

grid1 = [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0]
]
print(maxAreaOfIsland(grid1))  # Output: 5

grid2 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
print(maxAreaOfIsland(grid2))  # Output: 0

grid3 = [
    [1,1],
    [1,1]
]
print(maxAreaOfIsland(grid3))  # Output: 4

grid4 = [
    [0,1,0],
    [1,0,1],
    [0,1,0]
]
print(maxAreaOfIsland(grid4))  # Output: 1
