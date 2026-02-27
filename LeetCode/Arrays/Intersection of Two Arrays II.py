class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        hash_map = {}

        for i in range(len(nums1)):
            if nums1[i] not in hash_map:
                hash_map[nums1[i]] = 1
            else:
                hash_map[nums1[i]] += 1

        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                result.append(num)
                hash_map[num] -= 1
        return result