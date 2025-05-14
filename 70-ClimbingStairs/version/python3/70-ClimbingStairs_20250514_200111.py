# Last updated: 14/05/2025, 20:01:11
# Recursive with cache (memoization), array.
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        def climb(step: int):
            if step == 1:
                return 1
            if step == 2:
                return 2
            if cache[step]:
                return cache[step]
            result = climb(step - 1) + climb(step - 2)
            cache[step] = result
            return result
        return climb(n)