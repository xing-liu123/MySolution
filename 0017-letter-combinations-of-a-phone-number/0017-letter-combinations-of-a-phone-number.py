class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        keys = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        
        res = []
        path = []
        
        if len(digits) < 1:
            return res
        
        def backtracking(index):
            if index == len(digits):
                res.append(''.join(path))
                return
            
            for char in keys[int(digits[index]) - 2]:
                path.append(char)
                backtracking(index + 1)
                path.pop()
                
        backtracking(0)
        
        return res