class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        # [1,5,5,11]

        dp = [0] * n
        # [0,0,0,0]
        dp[0] = nums[0]
        # [1,0,0,0]
        for i in range(1,n):
            if dp[i - 1] == nums[i]:
                return True
            dp[i] = dp[i - 1] + nums[i]
        
        return False


# ai 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]