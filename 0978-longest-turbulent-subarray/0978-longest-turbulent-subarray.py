class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        count = 1

        prevDiff = arr[1] - arr[0]

        res = 2 if prevDiff != 0 else 1
        count = res

        for i in range(2, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff > 0:
                if prevDiff < 0:
                    count += 1
                else:
                    count = 2
            elif diff < 0:
                if prevDiff > 0:
                    count += 1
                else:
                    count = 2
            else:
                count = 1
            
            res = max(count, res)
            prevDiff = diff

        return res

                
