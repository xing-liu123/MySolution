class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self.addToFront(node)
            
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                nodeToRemove = self.tail.prev
                del self.cache[nodeToRemove.key]
                self._remove(nodeToRemove)
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.addToFront(newNode)
        else:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self.addToFront(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.head = Node()
#         self.tail = Node()
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def addToFront(self, node):
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node

#     def removeNode(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev

#     def get(self, key: int) -> int:
#         if not key in self.cache:
#             return -1
        
#         node = self.cache[key]
#         self.removeNode(node)
#         self.addToFront(node)

#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.val = value
#             self.removeNode(node)
#             self.addToFront(node)
#         else:
#             if len(self.cache) == self.capacity:
#                 nodeToRemove = self.tail.prev
#                 self.removeNode(nodeToRemove)
#                 del self.cache[nodeToRemove.key]

#             node = Node(key, value)
#             self.cache[key] = node
#             self.addToFront(node)