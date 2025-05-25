def is_safe(positions, row, col):
    for i in range(row):
        if positions[i] == col or abs(positions[i] - col) == abs(i - row):
            return False
    return True

def place_queens(positions, row, N, solutions):
    if row == N:
        list_form = tuple(pos + 1 for pos in positions)
        board = []

        for r in range(N):
            line = [' . '] * N
            line[positions[r]] = 'Q'
            board.append(''.join(line))

        solutions.append((list_form, board))
        return
    
    for col in range(N):
        if is_safe(positions, row, col):
            positions[row] = col
            place_queens(positions, row + 1, N, solutions)
            positions[row] = -1

def solve(n):
    solutions = []
    positions = [-1] * n
    place_queens(positions, 0, n, solutions)
    return solutions if solutions else ["no Solution"]
n = 4
solutions = solve(n)
for lists, board in solutions:
    for row in board:
        print(row)
    print(lists)
    print()

#  . Q .  . 
#  .  .  . Q
# Q .  .  . 
#  .  . Q . 
# (2, 4, 1, 3)

#  .  . Q . 
# Q .  .  . 
#  .  .  . Q
#  . Q .  . 
# (3, 1, 4, 2)