#Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        answer = [1] * l
        prefix = 1
        suffix = 1

        for i in range(l):
            answer[i] = prefix
            prefix *= nums[i]
        
        for i in range(l-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer