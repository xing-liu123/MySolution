class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        list = []
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return matrix[0]
        
        if n == 1:
            list = [item for row in matrix for item in row]
            return list

        status = 0

        top = 1
        left = 0
        right = n - 1
        bottom = m - 1

        i = 0
        j = 0
        while len(list) < m * n:
            print(list)
            list.append(matrix[i][j])
           
            if status == 0:
                j += 1
                if j == right:
                    right -= 1
                    status = 1
            elif status == 1:
                i += 1
                if i == bottom:
                    bottom -= 1
                    status = 2
            elif status == 2:
                j -= 1
                if j == left:
                    left += 1
                    status = 3
            else:
                i -= 1
                if i == top:
                    top += 1
                    status = 0
        
        return list
