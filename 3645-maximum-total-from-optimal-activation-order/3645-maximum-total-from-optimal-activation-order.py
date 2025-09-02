class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        combine = sorted(zip(value, limit), key= lambda x: (x[1], -x[0]))

        left = 0
        res = 0

        for right, (v, l) in enumerate(combine):
            if right < left:
                continue
            count = right - left
            if count < l:
                res += v
                count += 1

                while left < n and combine[left][1] <= count:
                    left += 1

            if left == n:
                break
        
        return res