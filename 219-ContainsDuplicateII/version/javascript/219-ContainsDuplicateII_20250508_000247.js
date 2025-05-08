// Last updated: 08/05/2025, 00:02:47
// Iterative with sliding window algorithm.
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let result = false
    let set = new Set()
    for (let i = 0; i < nums.length; i++) {
        if (set.size > k) {
            set.delete(nums[i - k - 1])
        }
        if (set.has(nums[i])) {
            return true
        }
        set.add(nums[i])
    }
    return result
};