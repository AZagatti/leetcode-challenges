# Last updated: 16/06/2025, 22:20:27
'''
-----
Using object and set.
-----
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        viewed = set()
        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] != t[i]:
                return False
            if s[i] not in mapping and t[i] in viewed:
                return False
            mapping[s[i]] = t[i]
            viewed.add(t[i])
        return True
