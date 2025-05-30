// Last updated: 29/05/2025, 21:42:46
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    let left = 0
    let right = s.length - 1
    let regex = /[^0-9a-z]/i
    while (left < right) {
        while (left < right && regex.test(s[left])) {
            left++
        }
        while (left < right && regex.test(s[right])) {
            right--
        }
        if (left < right && s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false
        }
        left++
        right--
    }
    return true
};