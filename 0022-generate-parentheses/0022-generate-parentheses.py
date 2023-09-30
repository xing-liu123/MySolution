class Solution:
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        global left
        global right
        global path
        global res
        left = 0
        right = 0
        path = ""
        res = []
        self.generate(n)

        return res

    def generate(self, n: int):
        global left
        global right
        global path
        global res

        if len(path) == 2 * n:
            res.append(path)
            return
        
        if (left < n):
            path += "("
            left += 1
            self.generate(n)
            left -= 1
            path = path[:-1]
        
        if (right < left):
            path += ")"
            right += 1
            self.generate(n)
            right -= 1
            path = path[:-1]