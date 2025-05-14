# Last updated: 14/05/2025, 20:10:15
# Recursive with cache (built-in lru_cache python cache).
from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def climb(step: int):
            if step == 1:
                return 1
            if step == 2:
                return 2
            return climb(step - 1) + climb(step - 2)
        return climb(n)