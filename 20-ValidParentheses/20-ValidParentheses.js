// Last updated: 29/05/2025, 21:43:03
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