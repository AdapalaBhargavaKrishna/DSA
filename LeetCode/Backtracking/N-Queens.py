class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()
        anti_diag = set()
        board = [['.'] * n for _ in range(n)]
        res = []

        def backtracking(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti_diag:
                    continue

                cols.add(c)
                diag.add(r - c)
                anti_diag.add(r + c)
                board[r][c] = 'Q'

                backtracking(r + 1)

                cols.remove(c)
                diag.remove(r - c)
                anti_diag.remove(r + c)
                board[r][c] = '.'

        backtracking(0)
        return res