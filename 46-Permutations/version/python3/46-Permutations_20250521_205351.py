# Last updated: 21/05/2025, 20:53:51
'''
-----
Backtrack.
-----
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current_permutation):
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
            else:
                for num in nums:
                    if num not in current_permutation:
                        current_permutation.append(num)
                        backtrack(current_permutation)
                        current_permutation.pop()
        backtrack([])
        return result
