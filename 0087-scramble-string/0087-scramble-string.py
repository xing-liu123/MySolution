from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):  # Quick check: must have same characters
            return False

        @lru_cache(None)  # Memoization to speed up recursion
        def check(s1, s2):
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):  # Quick character check
                return False

            n = len(s1)
            for i in range(1, n):  # Partition at index `i`
                left, right = s1[:i], s1[i:]
                left2, right2 = s2[:i], s2[i:]
                swapped_left, swapped_right = s2[-i:], s2[:-i]

                # Check both non-swapped and swapped cases
                if (check(left, left2) and check(right, right2)) or (check(left, swapped_left) and check(right, swapped_right)):
                    return True

            return False

        return check(s1, s2)

        