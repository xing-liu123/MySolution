class MyHashMap:

    def __init__(self, capacity=1000, load_factor_threshold=0.7):
        self.capacity = capacity
        self.backing_arr = [None] * self.capacity
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        self.deleted_marker = "DELETED"

    def hash(self, key: int):
        return key % self.capacity

    def nextPrime(self, n):
        def isPrime(x):
            if x < 2:
                return False
            
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False

            return True

        while not isPrime(n):
            n += 1

        return n


    def rehash(self):
        old_backing_arr = self.backing_arr
        self.capacity  = self.nextPrime(self.capacity * 2)

        self.backing_arr = [None] * self.capacity

        for item in old_backing_arr:
            if item is not None and item != self.deleted_marker:
                key, val = item
                self.put(key, val)



    def put(self, key: int, value: int) -> None:
        if self.size / self.capacity > self.load_factor_threshold:
            self.rehash()

        index = self.hash(key)
        i = 0

        while i < self.capacity:
            new_index = (index + i * i) % self.capacity

            if self.backing_arr[new_index] is None or self.backing_arr[new_index] == self.deleted_marker or self.backing_arr[new_index][0] == key:
                if self.backing_arr[new_index] is None or self.backing_arr[new_index] == self.deleted_marker:
                    self.size += 1

                self.backing_arr[new_index] = (key, value)
                return
            
            i += 1


    def get(self, key: int) -> int:
        index = self.hash(key)
        i = 0

        while i < self.capacity:
            new_index = (index + i * i) % self.capacity

            if self.backing_arr[new_index] is None:
                return -1
                
            if self.backing_arr[new_index][0] != self.deleted_marker and self.backing_arr[new_index][0] == key:
                return self.backing_arr[new_index][1]

            i += 1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        i = 0

        while i < self.capacity:
            new_index = (index + i * i) % self.capacity

            if self.backing_arr[new_index] is None:
                return

            if self.backing_arr[new_index] != self.deleted_marker and self.backing_arr[new_index][0] == key:
                self.backing_arr[new_index] = self.deleted_marker
                self.size -= 1
                return

            i += 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)