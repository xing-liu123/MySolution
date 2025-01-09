class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zero_counts_from_back = [0] * n
        zero_count = 0

        for idx in range(n - 1, -1, -1):
            if s[idx] == "0":
                zero_count += 1
            
            zero_counts_from_back[idx] = zero_count

        if zero_count == 0 or zero_count == n:
            return 0

        one_count = 0
        min_flip = min(zero_count, n - zero_count)
        
        for idx, char in enumerate(s):
            if char == "1":
                one_count += 1

            if idx < n - 1:
                min_flip = min(min_flip, one_count + zero_counts_from_back[idx + 1])

        return min_flip

            

