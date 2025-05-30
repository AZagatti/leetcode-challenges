# Last updated: 29/05/2025, 23:21:34
'''
-----
Using Counter and sorted.
-----
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(Counter(s).items()))].append(s)
        return list(res.values())