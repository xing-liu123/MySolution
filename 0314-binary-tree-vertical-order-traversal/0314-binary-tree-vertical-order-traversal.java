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
    public List<List<Integer>> verticalOrder(TreeNode root) {

        List<List<Integer>> res = new ArrayList<>();

        if (root == null) {
            return res;
        }

        Map<Integer, List<Integer>> map = new HashMap<>();

        Deque<TreeNode> nodes = new ArrayDeque<>();
        Deque<Integer> cols = new ArrayDeque<>();

        nodes.offer(root);
        cols.offer(0);

        while (!nodes.isEmpty()) {
            int size = nodes.size();

            while (size > 0) {
                TreeNode node = nodes.poll();
                int col = cols.poll();

                List<Integer> list = new ArrayList<>();

                if (map.containsKey(col)) {
                    list = map.get(col);
                }
                list.add(node.val);
                map.put(col, list);

                if (node.left != null) {
                    nodes.offer(node.left);
                    cols.offer(col - 1);
                }

                if (node.right != null) {
                    nodes.offer(node.right);
                    cols.offer(col + 1);
                }

                size--;
            }
        }
        

        List<Integer> keys = new ArrayList<>(map.keySet());


        Collections.sort(keys);

        for (int k : keys) {
            res.add(map.get(k));
        }

        return res;
    }

 
}