// Last updated: 07/05/2025, 22:29:09
// Recursive.
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
    const isRightLeftSymmetric = (left, right) => {
        if (!left && !right) {
            return true
        }
        if (left?.val !== right?.val) {
            return false
        }
        let isFirstSymmetric = isRightLeftSymmetric(left.left, right.right)
        let isRightSymmetric = isRightLeftSymmetric(left.right, right.left)
        return isFirstSymmetric && isRightSymmetric
    }
    const isBothSymmetric = isRightLeftSymmetric(root.left, root.right)
    return isBothSymmetric
};