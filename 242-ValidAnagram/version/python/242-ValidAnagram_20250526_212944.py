# Last updated: 26/05/2025, 21:29:44
'''
-----
Using for loop to get result.
-----
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            hash_map[t[i]] = hash_map.get(t[i], 0) - 1
        for value in hash_map.values():
            if value != 0:
                return False
        return True
