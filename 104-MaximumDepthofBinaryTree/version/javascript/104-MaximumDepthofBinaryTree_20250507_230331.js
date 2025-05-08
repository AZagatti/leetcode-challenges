// Last updated: 07/05/2025, 23:03:31
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
 * @return {number}
 */
var maxDepth = function(root) {
    if (root === null ) {
        return 0
    }
    let maxDepthRight = maxDepth(root.right)
    let maxDepthLeft = maxDepth(root.left)
    return 1 + Math.max(maxDepthRight, maxDepthLeft)
};