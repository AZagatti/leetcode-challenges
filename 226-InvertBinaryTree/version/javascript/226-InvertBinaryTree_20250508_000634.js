// Last updated: 08/05/2025, 00:06:34
// Iterative with queue.
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
 * @return {TreeNode}
 */
var invertTree = function (root) {
    let queue = [root]
    while (queue.length) {
        let item = queue.shift()
        if (!item) {
            continue
        }
        let tempLeft = item.left
        item.left = item.right
        item.right = tempLeft
        queue.push(item.left, item.right)
    }
    return root
};