
class MyCircularQueue {
    let capacity: Int
    var arr: [Int]
    var front = 0
    var rear = 0
    var size = 0

    init(_ k: Int) {
        capacity = k
        arr = Array(repeating: 0, count: k)
    }
    
    func enQueue(_ value: Int) -> Bool {
        if size == capacity {
            return false
        }

        arr[rear] = value
        rear = (rear + 1) % capacity
        size += 1

        return true
    }
    
    func deQueue() -> Bool {
        if size == 0 {
            return false
        }

        front = (front + 1) % capacity
        size -= 1

        return true
    }
    
    func Front() -> Int {
        if size == 0 {
            return -1
        }

        return arr[front]
    }
    
    func Rear() -> Int {
        if size == 0 {
            return -1
        }

        if rear == 0 {
            return arr.last!
        }

        return arr[rear - 1]
    }
    
    func isEmpty() -> Bool {
        return size == 0
    }
    
    func isFull() -> Bool {
        return size == capacity
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * let obj = MyCircularQueue(k)
 * let ret_1: Bool = obj.enQueue(value)
 * let ret_2: Bool = obj.deQueue()
 * let ret_3: Int = obj.Front()
 * let ret_4: Int = obj.Rear()
 * let ret_5: Bool = obj.isEmpty()
 * let ret_6: Bool = obj.isFull()
 */