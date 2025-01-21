class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in num_set:
                return i // 3 + 1
            
            num_set.add(nums[i])

        return 0