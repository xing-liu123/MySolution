/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    Node[] nodeArr = new Node[101];
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        } else {
            Node copy = new Node(node.val);
            nodeArr[copy.val] = copy;

            ArrayList<Node> neighborsCopy = new ArrayList<>();
            for (int i = 0; i < node.neighbors.size(); i++) {
                if (nodeArr[node.neighbors.get(i).val] != null) {
                    neighborsCopy.add(nodeArr[node.neighbors.get(i).val]);
                } else {
                    neighborsCopy.add(cloneGraph(node.neighbors.get(i)));
                }
                
            }
            copy.neighbors = neighborsCopy;

            return copy;
        }
    }
}