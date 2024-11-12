class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        currRow = 0
        currCol = 0
        currDirection = 0 # 0 for right, 1 for down, 2 for left, 3 for up
        top, bottom, left, right = 1, n - 1, 0, n - 1

        for num in range(1, n * n + 1):
            matrix[currRow][currCol] = num

            if currDirection == 0:
                if currCol == right:
                    currRow += 1
                    currDirection = 1
                    right -= 1
                else:
                    currCol += 1
            elif currDirection == 1:
                if currRow == bottom:
                    currCol -= 1
                    currDirection = 2
                    bottom -= 1
                else:
                    currRow += 1
            elif currDirection == 2:
                if currCol == left:
                    currRow -= 1
                    currDirection = 3
                    left += 1
                else:
                    currCol -= 1
            elif currDirection == 3:
                if currRow == top:
                    currCol += 1
                    currDirection = 0
                    top += 1
                else:
                    currRow -= 1
        
        return matrix


            
