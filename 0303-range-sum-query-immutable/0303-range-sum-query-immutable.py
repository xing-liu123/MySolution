class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums)
        self.prefixSum[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right] - self.prefixSum[left - 1] if left > 0 else self.prefixSum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)