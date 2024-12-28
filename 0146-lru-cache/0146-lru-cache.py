class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToFront(self, node: Node):
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
            self._remove(node)
            self.addToFront(node)
            node.val = value
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            node = Node(key, value)
            self.cache[key] = node
            self.addToFront(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)