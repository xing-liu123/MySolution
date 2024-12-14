class TwoSum:

    def __init__(self):
        self.nums = {}
        self.sums = set()

    def add(self, number: int) -> None:
        self.nums[number] = self.nums.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        for num in self.nums.keys():
            comple = value - num

            if comple != num:
                if comple in self.nums:
                    return True
            elif self.nums[num] > 1:
                return True

        return False

            


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)