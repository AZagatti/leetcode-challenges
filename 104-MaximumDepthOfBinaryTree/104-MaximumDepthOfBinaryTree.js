// Last updated: 29/05/2025, 21:42:51
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
    let depth = 0
    let queue = [root]
    let headQueueIndex = 0
    while (queue.length - headQueueIndex) {
        let levelSize = queue.length - headQueueIndex 
        for (let i = 0; i < levelSize; i++) {
            let item = queue[headQueueIndex]
            headQueueIndex += 1
            if (item.left) {
                queue.push(item.left)
            }
            if (item.right) {
                queue.push(item.right)
            }
        }
        depth += 1
    }
    return depth
};