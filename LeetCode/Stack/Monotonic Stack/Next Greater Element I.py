class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []  
        ng = {}

        for num in nums2:
            while stack and num > stack[-1]:
                ng[stack.pop()] = num
            stack.append(num)

        for num in stack:
            ng[num] = -1

        return [ng[num] for num in nums1]