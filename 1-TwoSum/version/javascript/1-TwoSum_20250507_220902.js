// Last updated: 07/05/2025, 22:09:02
/*
 * Bad solution.
 * O(n^2)
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let result = []
    nums.forEach((num, i) => {
        if (result.length === 2) return
        nums.forEach((num2, i2) => {
            if (i !== i2 && num + num2 === target) {
                result.push(i, i2)
            }
        })
    })
    return result
};