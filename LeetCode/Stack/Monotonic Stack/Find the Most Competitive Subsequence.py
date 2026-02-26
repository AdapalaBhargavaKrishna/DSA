class Solution(object):
    def mostCompetitive(self, nums, k):
        stack = []
        n = len(nums) - k
        for num in nums:
            while n and stack and num < stack[-1]:
                stack.pop()
                n -= 1
            stack.append(num)
        return stack[:k]