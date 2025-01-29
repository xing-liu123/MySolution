class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        numCount1 = {}
        numCount2 = {}
        res = []

        for i in range(len(A)):
            curr = 0 if len(res) == 0 else res[-1]
            if A[i] in numCount1:
                numCount1[A[i]] += 1
            else:
                if A[i] in numCount2:
                    curr += 1
                numCount1[A[i]] = 1
                

            if B[i] in numCount2:
                numCount2[B[i]] += 1
            else:
                if B[i] in numCount1:
                    curr += 1
                numCount2[B[i]] = 1
                
            res.append(curr)
 

        return res