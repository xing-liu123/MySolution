class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set()

        n = len(nums)
        
        idx = -1

        for i in range(n - 1, -1, -1):
            if nums[i] in num_set:
                idx = i
                break
            else:
                num_set.add(nums[i])
        
        if idx == -1:
            return 0
        else:
            return (i + 1 + 2) // 3

         