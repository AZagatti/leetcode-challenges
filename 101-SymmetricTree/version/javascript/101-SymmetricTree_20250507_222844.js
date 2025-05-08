// Last updated: 07/05/2025, 22:28:44
// Iterative with stack.
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
    const stack = [[root.left, root.right]]
    let result = true
    while (stack.length) {
        const item = stack.pop()
        const left = item[0]
        const right = item[1]
        if (left?.val !== right?.val) {
            result = false
            continue
        }
        if (!left || !right) {
            continue
        }
        stack.push([left.left, right.right], [left.right, right.left])
    }
    return result
};