# Last updated: 26/05/2025, 21:14:52
'''
-----
Using object Counter built-in Python.
-----
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
