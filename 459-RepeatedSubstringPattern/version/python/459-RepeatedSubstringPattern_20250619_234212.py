# Last updated: 19/06/2025, 23:42:12
'''
-----
One liner.
----
Regarding the s in (s+s)[1:-1] trick:

Just out of curiosity, this is a famous one-line solution in Python. It's O(N) in time and space, and it works because if s is composed of repetitions of a pattern t (e.g., s = "abab" -> t="ab"), then s+s will be "abababab". By removing the first and last character, we get "bababa", and the original string "abab" is still contained within it. If s is not a repeated pattern (e.g., "aba"), s+s is "abaaba", and (s+s)[1:-1] becomes "baab", which does not contain "aba". It's a very clever solution, but less intuitive than the one you implemented.
-----
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
