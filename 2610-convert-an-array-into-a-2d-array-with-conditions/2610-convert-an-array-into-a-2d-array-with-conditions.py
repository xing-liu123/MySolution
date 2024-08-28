class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numListMap = defaultdict(int)

        res = []

        for num in nums:
            idx = numListMap[num]
            if len(res) < idx + 1:
                res.append([])
            res[idx].append(num)
            numListMap[num] += 1
        
        return res
            

        