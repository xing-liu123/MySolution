class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            return [-1]

        curr_max = arr[-1]

        for i in range(n - 2, -1, -1):
            temp = curr_max
            curr_max = max(arr[i], curr_max)
            arr[i] = temp
        
        arr[-1] = -1

        return arr