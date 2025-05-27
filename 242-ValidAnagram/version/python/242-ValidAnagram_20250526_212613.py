# Last updated: 26/05/2025, 21:26:13
'''
-----
Using dict with 'all' method.
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
        return all(value == 0 for value in hash_map.values())            
