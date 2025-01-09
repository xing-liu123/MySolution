class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zero_count = s.count("0")

        if zero_count == 0 or zero_count == n:
            return 0

        min_flip = min(zero_count, n - zero_count)
        curr_one_count = 0
        
        for idx, char in enumerate(s):
            if char == "1":
                curr_one_count += 1

            remaining_zero_count = zero_count - (idx + 1 - curr_one_count)

            min_flip = min(min_flip, curr_one_count + remaining_zero_count)

        return min_flip

            

