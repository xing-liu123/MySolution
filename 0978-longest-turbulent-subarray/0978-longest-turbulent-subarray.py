class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        count = 1

        prevDiff = 0

        res = 1

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff == 0:
                count = 1
            elif diff < 0 and prevDiff > 0 or diff > 0 and prevDiff < 0:
                count += 1
            else:
                count = 2
            
            res = max(count, res)
            prevDiff = diff

        return res

                
