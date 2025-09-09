# Last updated: 08/09/2025, 22:42:23
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += pow(digit, 2)
                number //= 10
            return total_sum

        slow = n
        fast = n
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
