class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights) , sum(weights)

        def feasible(cap):
            days_count = 1
            curr = 0

            for w in weights:
                if curr + w >  cap:
                    days_count += 1
                    curr = 0
                curr += w   
            return days_count <= days        


        while low < high:

            mid = low + (high - low) // 2

            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low