class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.prev = None
        self.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.head.count = float('-inf')
        self.tail = Node(-1, -1)
        self.tail.count = float('inf')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lastValNode = {}

    def update(self, node):
        count = node.count

        if count in self.lastValNode:
            if count - 1 in self.lastValNode and self.lastValNode[count - 1].key == node.key:
                if node.prev.count == count - 1:
                    self.lastValNode[count - 1] = node.prev
                else:
                    del self.lastValNode[count - 1]

            lastNode = self.lastValNode[count]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = lastNode.next
            node.prev = lastNode
            lastNode.next.prev = node
            lastNode.next = node

            
        
        elif count - 1 in self.lastValNode:

            lastNode = self.lastValNode[count - 1]
            if lastNode.key != node.key:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = lastNode.next
                node.prev = lastNode
                lastNode.next.prev = node
                lastNode.next = node
            else:
                if node.prev.count == count - 1:
                    self.lastValNode[count - 1] = node.prev
                else:
                    del self.lastValNode[count - 1]

        self.lastValNode[count] = node
    
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        node.count += 1

        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.count += 1
            self.update(node)
        else:
            if self.capacity == len(self.cache):
                nodeToRemove = self.head.next
                del self.cache[nodeToRemove.key]
                if nodeToRemove.count in self.lastValNode:
                    if self.lastValNode[nodeToRemove.count].key == nodeToRemove.key:
                        del self.lastValNode[nodeToRemove.count]
      
                nodeToRemove.prev.next = nodeToRemove.next
                nodeToRemove.next.prev = nodeToRemove.prev
                
            node = Node(key, value)
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            self.update(node)
            self.cache[key] = node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)