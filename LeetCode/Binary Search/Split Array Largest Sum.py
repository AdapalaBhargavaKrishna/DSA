class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low , high = max(nums) , sum(nums)

        def feasible(mid):
            count = 1
            curr = 0
            for num in nums:
                if curr + num > mid:
                    count += 1
                    curr = 0
                curr += num

            return count <= k

        while low < high:
            mid = low + (high - low) // 2

            if feasible(mid):
                high = mid
            else:
                low = mid + 1

        return low