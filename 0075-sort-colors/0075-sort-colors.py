class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def switch(left, right):
            nums[left], nums[right] = nums[right], nums[left]

        def partition(left, right):
            pivot = nums[right]
            i = left - 1

            for j in range(left, right):
                if nums[j] < pivot:
                    i += 1
                    switch(i, j)
            switch(i + 1, right)

            return i + 1

        def quicksort(left, right):
            if left < right:
                mid = partition(left, right)
                quicksort(left, mid - 1)
                quicksort(mid + 1, right)
        
        quicksort(0, len(nums) - 1)