class Solution:
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.left = 0
        self.right = 0
        self.path = ""
        self.res = []
        self.max = n
        self.generate()

        return self.res

    def generate(self):
        if len(self.path) == 2 * self.max:
            self.res.append(self.path)
            return
        
        if (self.left < self.max):
            self.path += "("
            self.left += 1
            self.generate()
            self.left -= 1
            self.path = self.path[:-1]
        
        if (self.right < self.left):
            self.path += ")"
            self.right += 1
            self.generate()
            self.right -= 1
            self.path = self.path[:-1]