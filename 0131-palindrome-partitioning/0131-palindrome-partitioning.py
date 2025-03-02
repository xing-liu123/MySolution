class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1

            return True

        res = []
        partition = []

        def backtracking(idx):
            if idx == len(s):
                res.append(copy.copy(partition))
                return

            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    partition.append(s[idx: i + 1])
                    backtracking(i + 1)
                    partition.pop()

        backtracking(0)

        return res