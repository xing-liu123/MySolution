class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        
        if len(s) < 4 or len(s) > 12:
            return res
        
        def backtracking(start):
            if start == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            
            if start == len(s) or len(path) == 4:
                return
        
            
            for length in range(1, 4):
                if start + length > len(s):
                    return
                
                segment = s[start: start + length]
                
                if isValid(segment):
                    path.append(segment)
                    backtracking(start + length)
                    path.pop()
          
        def isValid(num: str) -> bool:
            if len(num) > 1 and num[0] == '0':
                return False
            
            num_int = int(num)
            return 0 <= num_int <= 255
            
        backtracking(0)
        return res
 