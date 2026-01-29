class Solution(object):
    def intersection(self, nums1, nums2):
        n=len(nums1)
        hash_map={}
        res=[]
        for i in range(n):
            if nums1[i] not in hash_map:
                hash_map[nums1[i]]=1
        for num in nums2:
            if num in hash_map and hash_map[num]==1:
                res.append(num)
                hash_map[num]+=1
        return res
        