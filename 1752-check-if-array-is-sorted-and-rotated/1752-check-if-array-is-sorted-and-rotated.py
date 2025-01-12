class Solution:
    def check(self, nums: List[int]) -> bool:
        rotate_found = False
        min_val, max_val = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if rotate_found:
                    return False
                else:
                    rotate_found = True
            
            elif not rotate_found:
                max_val = nums[i]
            
            if rotate_found:
                if min_val == max_val and nums[i] > max_val or min_val != max_val and min_val < nums[i] < max_val:
                    return False
            

        return True