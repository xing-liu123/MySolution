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
var rob = function(root) {
    const helper = (node) => {
        let dp = [0, 0];
        
        if (node === null) {
            return dp;
        }
        
        let left = helper(node.left);
        let right = helper(node.right);
        
        dp[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        dp[1] = node.val + left[0] + right[0];
        
        return dp;
    }
    
    let res = helper(root);
    return Math.max(res[0], res[1]);
};