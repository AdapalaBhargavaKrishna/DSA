class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        res = set()
        left = 0
        right = 1
        min_diff = float('inf')
        while right < len(arr):
            if abs(arr[left] - arr[right]) < min_diff:
                min_diff = abs(arr[left] - arr[right])
                res = [[arr[left], arr[right]]]
            elif abs(arr[left] - arr[right]) == min_diff:
                res.append([arr[left], arr[right]])
            left += 1
            right += 1
        return list(res)