// Last updated: 07/05/2025, 22:11:46
/*
 * Good solution.
 * O(n)
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    for (let i = 0; i < s.length; i++) {
        if (stack.at(-1) === s[i]) {
            stack.pop()
        } else if (s[i] === '(') {
            stack.push(')')
        } else if (s[i] === '[') {
            stack.push(']')
        } else if (s[i] === '{') {
            stack.push('}')
        } else {
            return false
        }
    }
    return !stack.length
};