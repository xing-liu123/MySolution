class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False


        def search(left, right, top, bottom):
            if left > right or top > bottom:
                return False
            
            col = (left + right) // 2
            row = (top + bottom) // 2
            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                return (search(left, right, top, row - 1) or search(left, col - 1, row, bottom))       
            else:
                return (search(left, right, row + 1, bottom) or search(col + 1, right, top, row))


        return search(0, n - 1, 0, m - 1)
                    
                    


                

