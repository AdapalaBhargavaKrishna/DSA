def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    q, fresh = [], 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    time = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    head = 0

    while head < len(q) and fresh:
        
        for _ in range(len(q) - head):
            r, c = q[head]; head += 1

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        time += 1

    return time if fresh == 0 else -1

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
print(orangesRotting([[0,2]]))                    # 0