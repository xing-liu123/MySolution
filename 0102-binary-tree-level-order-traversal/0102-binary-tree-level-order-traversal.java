/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // LinkedList<List<Integer>> res = new LinkedList<>();

        // if (root == null) {
        //     return res;
        // }

        // Queue<TreeNode> queue = new LinkedList<>();

        // queue.offer(root);

        // while(!queue.isEmpty()) {
        //     List<Integer> list = new LinkedList<>();

        //     int size = queue.size();
            

        //     while(size > 0) {
        //         TreeNode node = queue.poll();
        //         if (node.left != null) {
        //             queue.offer(node.left);
        //         }
        //         if (node.right != null) {
        //             queue.offer(node.right);
        //         }
        //         list.add(node.val);
        //         size--;
        //     }
        //     res.add(list);
        // } 
        // return res;
        List<List<Integer>> res = new ArrayList<>();
        traverse(res, root, 0);
        return res;
    }

    private void traverse(List<List<Integer>> list, TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        if (depth == list.size()) {
            list.add(new ArrayList<>());
        }
        
        list.get(depth).add(node.val);
        traverse(list, node.left, depth + 1);
        traverse(list, node.right, depth + 1);
    }
}