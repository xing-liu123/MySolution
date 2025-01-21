class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set(num for num in nums if num != 0)

        return len(num_set)