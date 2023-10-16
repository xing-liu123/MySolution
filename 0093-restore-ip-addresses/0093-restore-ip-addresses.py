class Solution:
    def __init__(self):
        self.ip = ""
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ip = s
        self.backtracking(0, 0)
        return self.res
    
    def backtracking(self, countDot: int, idx: int):
        if countDot == 3:
            if self.isValid(idx, len(self.ip) - 1):
                self.res.append(copy.copy(self.ip))
            return
        
        for i in range(idx, len(self.ip)):
            if self.isValid(idx, i):
                self.ip = self.ip[: i+1] + "." + self.ip[i+1:]
                self.backtracking(countDot + 1, i + 2)
                self.ip = self.ip[: i+1] + self.ip[i+2 :]
            else:
                break
    
    def isValid(self, start: int, end: int) -> bool:
        if start > end:
            return False
        
        if self.ip[start] == '0' and start != end:
            return False
        
        return int(self.ip[start: end + 1]) >= 0 and int(self.ip[start: end + 1]) <= 255
        