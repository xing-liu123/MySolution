class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        left = 0
        right = n - 1
        mod = 10 ** 9 + 7

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += (2 ** (right - left)) % mod
                count %= mod
                left += 1

        return count