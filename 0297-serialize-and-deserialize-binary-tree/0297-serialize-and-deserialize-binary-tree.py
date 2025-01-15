# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(','))  # Create an iterator for the values

        def build():
            val = next(values)
            if val == "#":
                return None  # Null node

            node = TreeNode(int(val))  # Create a new node
            node.left = build()  # Recursively build the left subtree
            node.right = build()  # Recursively build the right subtree
            return node

        return build()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))