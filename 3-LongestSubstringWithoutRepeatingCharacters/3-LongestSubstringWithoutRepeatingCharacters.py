# Last updated: 29/05/2025, 21:43:02
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        chars = {}
        max_length = 0
        for idx, char in enumerate(s):
            if s[right] in chars and chars[s[right]] >= left:
                left = chars[s[right]] + 1
            right += 1
            chars[char] = idx
            if len(s[left:right]) > max_length:
                max_length = len(s[left:right])
        return max_length
