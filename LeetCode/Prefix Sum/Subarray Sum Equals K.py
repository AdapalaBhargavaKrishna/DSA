class Solution(object):
    def subarraySum(self, nums, k):
        result = 0
        prefix_sum = 0
        mp = {0 : 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in mp:
                result += mp[prefix_sum - k]
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
            
        return result

class Solution(object):
    def subarraySum(self, nums, k):
        mp={0:1}
        count=0
        prefix=0
        for i in nums:
            prefix+=i
            if prefix-k in mp:
                count+=mp[prefix-k]
            if prefix in mp:
                mp[prefix]+=1
            else:
                mp[prefix]=1
        return count


# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2