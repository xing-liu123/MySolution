
class MyHashMap {
    var capacity = 10
    var backingArray: [(key: Int, value: Int)?]
    var size = 0
    let factor = 0.65

    init() {
        backingArray = Array(repeating: nil, count: capacity)
    }

    private func hash(_ key: Int) -> Int{
        return abs(key.hashValue) % capacity
    }

    private func resize() {
        let oldArray = backingArray
        capacity *= 2
        size = 0
        backingArray = Array(repeating: nil, count: capacity)

        for entry in oldArray {
            if let (key, value) = entry, key != -1 {
                put(key, value)
            }
        }

    }
    
    func put(_ key: Int, _ value: Int) {
        if Double(size + 1) / Double(capacity) > factor {
            resize()
        }

        var index = hash(key)

        while let entry = backingArray[index] {
            if entry.key == key {
                backingArray[index] = (key, value)
                return
            }

            if entry.key == -1 {
                break
            }
            index = (index + 1) % capacity
        }

        backingArray[index] = (key, value)
        size += 1
    }
    
    func get(_ key: Int) -> Int {
        var index = hash(key)
        let indexCopy = index

        while let entry = backingArray[index] {
            if entry.key == key {
                return entry.value
            }

            index = (index + 1) % capacity

            if index == indexCopy {
                return -1
            }
        }

        return -1
    }
    
    func remove(_ key: Int) {
        var index = hash(key)

        while let entry = backingArray[index] {
            if entry.key == key {
                backingArray[index] = (-1, -1)
                size -= 1
                return
            }

            index = (index + 1) % capacity
        }

    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap()
 * obj.put(key, value)
 * let ret_2: Int = obj.get(key)
 * obj.remove(key)
 */