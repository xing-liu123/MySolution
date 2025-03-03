
class Node {
    let key: Int
    var val: Int
    var next: Node?
    var prev: Node?

    init(_ key: Int = -1, _ val: Int = -1) {
        self.key = key
        self.val = val
    }
}

class LRUCache {
    let capacity: Int
    var cache: [Int: Node] = [:]
    var head: Node
    var tail: Node

    init(_ capacity: Int) {
        self.capacity = capacity
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev = head
    }

    func removeNode(_ node: Node) {
        node.prev?.next = node.next
        node.next?.prev = node.prev
    }

    func addNodeToFront(_ node: Node) {
        node.next = head.next
        node.prev = head.next?.prev
        head.next?.prev = node
        head.next = node
    }
    
    func get(_ key: Int) -> Int {
        if let node = self.cache[key] {
            removeNode(node)
            addNodeToFront(node)
            return node.val
        }

        return -1
    }
    
    func put(_ key: Int, _ value: Int) {
        if let node = self.cache[key] {
            node.val = value
            removeNode(node)
            addNodeToFront(node)
            return
        }

        if self.cache.count == self.capacity {
            if let lastNode = self.tail.prev {
                self.cache.removeValue(forKey: lastNode.key)
                removeNode(lastNode)
            }
        }

        var newNode = Node(key, value)
        self.cache[key] = newNode
        addNodeToFront(newNode)
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */