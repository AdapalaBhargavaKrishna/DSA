class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        from collections import Counter

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        res = [-1,-1]
        res_len = float('inf')

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                window[s[left]] -=1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l,r = res

        return s[l:r+1] if res_len != float("inf") else ""

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.