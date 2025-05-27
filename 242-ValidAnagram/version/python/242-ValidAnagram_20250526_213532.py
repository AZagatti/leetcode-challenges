# Last updated: 26/05/2025, 21:35:32
'''
-----
Using sorted.
-----
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)