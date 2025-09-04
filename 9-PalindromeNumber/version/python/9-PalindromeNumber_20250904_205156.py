# Last updated: 04/09/2025, 20:51:56
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        inverted = ""
        temp = x
        while temp:
            inverted += str(temp % 10)
            temp //= 10
        return x == int(inverted)
    