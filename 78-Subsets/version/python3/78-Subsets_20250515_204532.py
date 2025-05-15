# Last updated: 15/05/2025, 20:45:32
'''
-----
Recursive with backtracking.
-----
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def backtrack(index, current_subset):
            all_subsets.append(current_subset.copy())
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
        backtrack(0, [])
        return all_subsets
