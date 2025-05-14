# Last updated: 14/05/2025, 19:50:21
# Recursive with cache (memoization).
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(step: int):
            nonlocal cache
            if step == 1:
                return 1
            if step == 2:
                return 2
            if step in cache:
                return cache[step]
            result = climb(step - 1) + climb(step - 2)
            cache[step] = result
            return result
        return climb(n)