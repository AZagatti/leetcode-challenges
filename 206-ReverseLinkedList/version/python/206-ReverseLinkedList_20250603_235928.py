# Last updated: 03/06/2025, 23:59:28
'''
-----
Merge sort.
-----
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            merged_arr = []
            pointer_arr1 = 0
            pointer_arr2 = 0
            while pointer_arr1 < len(arr1) and pointer_arr2 < len(arr2):
                if arr1[pointer_arr1] < arr2[pointer_arr2]:
                    merged_arr.append(arr1[pointer_arr1])
                    pointer_arr1 += 1
                else:
                    merged_arr.append(arr2[pointer_arr2])
                    pointer_arr2 += 1
            if pointer_arr1 < len(arr1):
                return merged_arr + arr1[pointer_arr1:]
            if pointer_arr2 < len(arr2):
                return merged_arr + arr2[pointer_arr2:]

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            n = len(arr) // 2
            left_half = arr[:n]
            right_half = arr[n:]
            sorted_left_half = mergeSort(left_half)
            sorted_right_half = mergeSort(right_half)
            return merge(sorted_left_half, sorted_right_half)

        return mergeSort(nums)