class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      
        def quickselect(nums: List[int], k: int) -> int:
            pivotVal = random.choice(nums)  # randomly select a pivot

            left = [num for num in nums if num > pivotVal]
            mid = [num for num in nums if num == pivotVal]
            right = [num for num in nums if num < pivotVal]

            if k <= len(left):
                return quickselect(left, k)
            
            if k > len(left) + len(mid):
                return quickselect(right, k - len(left) - len(mid))
            
            return pivotVal
        
        return quickselect(nums, k)
    

