class Solution:
    def maxProduct(self, s: str) -> int:
        res = 0

        def isPalindrome(sub):
            left, right = 0, len(sub) - 1

            while left < right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        def backtracking(sub1, sub2, idx):
            nonlocal res
            if idx == len(s):
                if isPalindrome(sub1) and isPalindrome(sub2):
                    res = max(res, len(sub1) * len(sub2))

                return

            backtracking(sub1 + s[idx], sub2, idx + 1)
            backtracking(sub1, sub2 + s[idx], idx + 1)
            backtracking(sub1, sub2, idx + 1)
        
        backtracking("", "", 0)

        return res

