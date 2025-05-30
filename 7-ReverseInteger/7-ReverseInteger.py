# Last updated: 29/05/2025, 21:43:01
class Solution:
    def reverse(self, x: int) -> int:
        is_positive = x > 0
        MAX_INT = 2**31 -1
        MIN_INT = -2**31
        val = abs(x)
        rev = 0
        while val > 0:
            digit = val % 10
            val //= 10
            if rev > MAX_INT // 10:
                return 0    
            if is_positive and rev == MAX_INT // 10 and digit > MAX_INT % 10:
                return 0
            if not is_positive and rev == abs(MIN_INT) // 10 and digit > abs(MIN_INT) % 10:
                return 0
            rev = rev * 10 + digit
        return rev if is_positive else -rev
    