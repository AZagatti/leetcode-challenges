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