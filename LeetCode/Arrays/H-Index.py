class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse = True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h += 1
            else:
                break
        return h
    
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.