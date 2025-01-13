class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def compute(div):

            res = 0
            for num in nums:
                res += (num - 1) // div + 1

            return res

        while left <= right:
            mid = (left + right) // 2

            res = compute(mid)

            if res > threshold:
                left = mid + 1
            else:
                right = mid - 1

        return left
            

