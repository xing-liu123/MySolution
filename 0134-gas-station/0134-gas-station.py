class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        currRemain = 0
        totalRemain = 0

        for i in range(len(gas)):
            currRemain += gas[i] - cost[i]
            totalRemain += gas[i] - cost[i]

            if currRemain < 0:
                start = i + 1
                currRemain = 0
        
        if totalRemain < 0:
            return -1
       
        return start