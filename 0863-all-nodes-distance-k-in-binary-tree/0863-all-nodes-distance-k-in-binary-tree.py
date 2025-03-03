# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def buildGraph(curr, parent=None):
            if not curr:
                return

            if parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)

            buildGraph(curr.left, curr)
            buildGraph(curr.right, curr)

        buildGraph(root)

        queue = deque([target.val])

        res = []
        visited = set([target.val])

        while queue and k >= 0:
            size = len(queue)

            for _ in range(size):
                val = queue.popleft()

                if k == 0:
                    res.append(val)
                else:

                    for nextVal in graph[val]:
                        if not nextVal in visited:
                            visited.add(nextVal)
                            queue.append(nextVal)

            k -= 1

        return res