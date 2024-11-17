class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currCost = 0
        currGas = 0
        minDiff = 0

        for i in range(len(gas)):
            currCost += cost[i]
            currGas += gas[i]
            minDiff = min(minDiff, currGas - currCost)
        
        if currCost > currGas:
            return -1
        
        if minDiff >= 0:
            return 0

        currCost = 0
        currGas = 0

        for i in range(len(gas) - 1, -1, -1):
            currCost += cost[i]
            currGas += gas[i]

            if currGas - currCost + minDiff >= 0:
                return i

        return 0