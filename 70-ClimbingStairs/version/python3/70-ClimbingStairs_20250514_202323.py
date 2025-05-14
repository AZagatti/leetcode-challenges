# Last updated: 14/05/2025, 20:23:23
# Iterative, Bottom-Up DP, Tabulation.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2    
        table = [0, 1, 2]
        for i in range(3, n + 1):
            table.append(table[i-1] + table[i-2])
        return table[-1]