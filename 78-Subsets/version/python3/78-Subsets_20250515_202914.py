# Last updated: 15/05/2025, 20:29:14
'''
===
Recursive with Backtracking.
===
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        current_subset = []
        def backtrack(index, current_subset):
            all_subsets.append(current_subset.copy())
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
            return all_subsets
        backtrack(0, current_subset)
        return all_subsets