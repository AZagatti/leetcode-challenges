# Last updated: 29/05/2025, 21:42:22
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)