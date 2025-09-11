# Last updated: 10/09/2025, 23:24:10
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        return 9 if num % 9 == 0 else num % 9
