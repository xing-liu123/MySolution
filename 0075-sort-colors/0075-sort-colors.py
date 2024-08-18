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

        def quickSort(left, right):
            if left < right:
                pi = partition(left, right)
                quickSort(left, pi - 1)
                quickSort(pi + 1, right)

        quickSort(0, len(nums) - 1)