class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            res = ''.join(sorted(s))
            ans[res].append(s)

        return list(ans.values())