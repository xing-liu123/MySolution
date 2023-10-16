class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.res
    
    def backtracking(self, s: str, idx: int):
        if idx == len(s):
            self.res.append(copy.copy(self.path))
            return
        
        for i in range(idx, len(s)):
            if self.isPalindrome(s[idx : i + 1]):
                self.path.append(s[idx : i + 1])
                self.backtracking(s, i + 1)
                self.path.pop()
        
    
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        
        return True