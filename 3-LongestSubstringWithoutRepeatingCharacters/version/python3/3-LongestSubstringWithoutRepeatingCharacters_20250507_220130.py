# Last updated: 07/05/2025, 22:01:30
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = {}
        max_length = 0
        for idx, char in enumerate(s):
            if char in chars and chars[char] >= left:
                left = chars[char] + 1
            chars[char] = idx
            current_length = idx - left + 1
            max_length = max(max_length, current_length)
        return max_length
