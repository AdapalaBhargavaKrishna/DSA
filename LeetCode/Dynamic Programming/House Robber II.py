class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(arr):
            prev2 , prev1 = 0, 0
            for num in arr:
                curr = max(prev1 , prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )