// Last updated: 29/05/2025, 21:42:19
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let left = 0
    let right = nums.length - 1
    while (left <= right) {
        let middle = Math.floor((left + right) / 2)
        if (nums[middle] === target) {
            return middle
        }
        if (nums[middle] < target) {
            left = middle + 1
        }
        if (nums[middle] > target) {
            right = middle - 1
        }
    }
    return -1
};