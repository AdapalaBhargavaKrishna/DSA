def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    queue = []
    fresh = 0
    time = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    head = 0

    while head < len(queue) and fresh > 0:
        level_size = len(queue) - head
        for _ in range(level_size):
            r, c = queue[head]
            head += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        time += 1

    return time if fresh == 0 else -1

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
print(orangesRotting([[0,2]]))                    # 0