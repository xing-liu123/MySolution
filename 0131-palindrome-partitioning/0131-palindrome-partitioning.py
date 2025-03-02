class Solution: 
    def __init__(self):
        self.path = []
        self.res = []
        
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.res
        
    def backtracking(self, s: str, start: int):
        if start == len(s):
            self.res.append(self.path.copy())
            return
        
        for i in range(start, len(s)):
            if self.isPalindrome(s[start: i + 1]):
                self.path.append(s[start: i + 1])
                self.backtracking(s, i + 1)
                self.path.pop()
    
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        