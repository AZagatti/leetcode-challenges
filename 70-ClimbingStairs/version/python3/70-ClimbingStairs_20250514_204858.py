# Last updated: 14/05/2025, 20:48:58
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step_before = 2
        two_steps_before = 1
        for i in range(3, n + 1):
            temp = one_step_before
            one_step_before = two_steps_before + one_step_before
            two_steps_before = temp
        return one_step_before