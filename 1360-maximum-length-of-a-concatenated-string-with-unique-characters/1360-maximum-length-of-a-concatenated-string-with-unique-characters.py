class Solution:
    def __init__(self):
        self.maxLen = 0
        self.currLen = 0
        self.used = [0] * 26

    def maxLength(self, arr: List[str]) -> int:
        self.backtracking(arr, 0)
        return self.maxLen
    
    def backtracking(self, arr: List[str], idx: int):
        self.maxLen = max(self.maxLen, self.currLen)

        if idx == len(arr):
            return
        
        for i in range(idx, len(arr)):
            if self.isValid(arr[i]):
                self.currLen += len(arr[i])
                for j in range(len(arr[i])):
                    self.used[ord(arr[i][j]) - ord('a')] = 1
                self.backtracking(arr, i + 1)
                self.currLen -= len(arr[i])
                for j in range(len(arr[i])):
                    self.used[ord(arr[i][j]) - ord('a')] = 0
    
    def isValid(self, s: str) -> bool:
        counts = [0] * 26
        for i in range(len(s)):
            if self.used[ord(s[i]) - ord('a')] > 0 or counts[ord(s[i]) - ord('a')]:
                return False
            counts[ord(s[i]) - ord('a')] += 1

        return True