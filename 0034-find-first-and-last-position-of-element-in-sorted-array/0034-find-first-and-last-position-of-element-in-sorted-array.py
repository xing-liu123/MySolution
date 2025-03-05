class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if len(nums) == 0:
        #     return [-1, -1]

        # left = bisect.bisect_left(nums, target)
        # right = bisect.bisect_right(nums, target)

        # if left == len(nums) or nums[left] != target:
        #     return [-1, -1]
            
        # return [left, right - 1]

        if len(nums) == 0:
            return [-1, -1]
        n = len(nums)
        left, right = 0, n - 1
        res = [-1, -1]
        isFound = False

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                isFound = True
                right = mid - 1

        if not isFound:
            return [-1, -1]

        res[0] = left

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                isFound = True
                left = mid + 1

        res[1] = right

        return res


        