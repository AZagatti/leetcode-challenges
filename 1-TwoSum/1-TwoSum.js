// Last updated: 29/05/2025, 21:43:05
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let result = []
    let cache = new Map()
    nums.forEach((num, i) => {
        if (result.length === 2) return
        let cachedNumber = cache.get(target - num)
        if (cachedNumber !== undefined && cachedNumber !== i) {
            return result.push(i, cachedNumber)
        }
        cache.set(num, i)
    })
    return result
};