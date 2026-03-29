class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            if total > target:
                return

            for i in range(start , len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtracking(i + 1, curr , total + candidates[i])
                curr.pop()

        backtracking(0,[],0)
        return res