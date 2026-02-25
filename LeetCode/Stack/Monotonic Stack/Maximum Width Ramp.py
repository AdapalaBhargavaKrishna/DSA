class Solution(object):
    def maxWidthRamp(self, nums):
        stack = []
        n = len(nums)

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        max_diff = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_diff = max(max_diff , j - stack.pop())

        return max_diff