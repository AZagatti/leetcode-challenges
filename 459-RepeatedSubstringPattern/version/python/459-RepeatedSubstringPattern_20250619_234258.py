# Last updated: 19/06/2025, 23:42:58
'''
-----
Using divisible and pattern.
-----
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                candidate = s[:i]
                complete = candidate * (n // i)
                if complete == s:
                    return True
        return False
