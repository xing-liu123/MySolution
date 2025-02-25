class Node:

    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToFront(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self.addToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self.addToFront(node)

        else:
            if len(self.cache) == self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]

            newNode = Node(key, value)
            self.cache[key] = newNode
            self.addToFront(newNode)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)