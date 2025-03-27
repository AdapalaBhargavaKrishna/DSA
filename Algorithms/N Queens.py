def is_safe(positions, row, col):
    for i in range(row):
        if positions[i] == col or abs(positions[i] - col) == abs(i - row):
            return False
    return True

def place_queens(positions, row, N, solutions):
    if row == N:
        solutions.append(tuple(pos + 1 for pos in positions))
        return
    for col in range(N):
        if is_safe(positions, row, col):
            positions[row] = col
            place_queens(positions, row + 1, N, solutions)
            positions[row] = -1

def solve(n):
    solutions = []
    positions =[-1] * n
    place_queens(positions, 0, n, solutions)
    return solutions if solutions else ["no Solution Selected"]

n = 4
solution = solve(n)
for i in solution:
    print(i)