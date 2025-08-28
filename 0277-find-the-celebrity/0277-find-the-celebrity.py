# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        canBe = [True] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                know = knows(i, j)
                if know:
                    canBe[i] = False
                    break
                else:
                    canBe[j] = False

        for i in range(n):
            if canBe[i]:
                isValid = True
                for j in range(n):
                    if not knows(j, i):
                        isValid = False
                        canBe[j] = False
                        break
                if isValid:

                    return i
        
        return -1
            
