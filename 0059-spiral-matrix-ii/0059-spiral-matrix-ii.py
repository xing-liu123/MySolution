class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        i = 0
        j = 0
        
        status = 1
        
        top = 1
        bottom = n - 1
        left = 0
        right = n - 1
        
        for count in range(n ** 2):
            matrix[i][j] = count + 1
            
            if status == 1:
                j += 1
                if j == right:
                    status = 2
                    right -=1
            elif status == 2:
                i += 1
                if i == bottom:
                    status = 3
                    bottom -= 1
            elif status == 3:
                j -= 1
                if j == left:
                    status = 4
                    left += 1
            else:
                i -= 1
                if i == top:
                    status = 1
                    top += 1
        
        return matrix
            
        