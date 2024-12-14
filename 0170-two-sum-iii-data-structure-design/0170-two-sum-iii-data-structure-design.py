class TwoSum:

    def __init__(self):
        self.nums = {}
        self.sums = set()

    def add(self, number: int) -> None:
        if number in self.nums and self.nums[number] > 1:
            return
        
        for num in self.nums:
            self.sums.add(number + num)

        self.nums[number] = self.nums.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        return value in self.sums
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)