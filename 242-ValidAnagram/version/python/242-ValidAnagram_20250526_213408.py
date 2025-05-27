# Last updated: 26/05/2025, 21:34:08
'''
-----
Using two dict's.
-----
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency_s = {}
        frequency_t = {}
        for i in range(0, len(s)):
            frequency_s[s[i]] = 1 + frequency_s.get(s[i], 0)
            frequency_t[t[i]] = 1 + frequency_t.get(t[i], 0)
        for key in frequency_s:
            if frequency_s[key] != frequency_t.get(key, 0):
                return False
        return True