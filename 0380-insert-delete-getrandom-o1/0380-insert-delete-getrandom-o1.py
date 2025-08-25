class RandomizedSet:
    
    def __init__(self):
        self.val_to_index = {}
        self.val_list = []


    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.val_list)
        self.val_list.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            index = self.val_to_index[val]
            last_val = self.val_list[-1]
            # last_val_index = self.val_to_index[last_val]
            self.val_list[index] = last_val
            self.val_to_index[last_val] = index
            self.val_list.pop()
            del self.val_to_index[val]
            return True

        return False
    

    def getRandom(self) -> int:
        return random.choice(self.val_list)

        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()