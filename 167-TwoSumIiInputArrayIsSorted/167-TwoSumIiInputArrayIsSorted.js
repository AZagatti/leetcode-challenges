// Last updated: 29/05/2025, 21:42:41
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let left = 0
    let right = numbers.length - 1
    let result = []
    while (left < right) {
        let sum = numbers[left] + numbers[right]
        if (sum < target) {
            left++
            continue
        }
        if (sum > target) {
            right--
            continue
        }
        if (left < right && sum === target) {
            result.push(left + 1, right + 1)
            break
        }
    }
    return result
};