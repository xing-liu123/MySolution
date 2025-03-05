class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitSums = defaultdict(list)

        res = -1

        for num in nums:
            digitSum = sum(int(val) for val in str(num))
            numList = digitSums[digitSum]
            if len(numList) == 0:
                numList.append(num)
            elif len(numList) == 1:
                numList.append(num)
                res = max(res, numList[0] + numList[1])
            elif len(numList) == 2:
                if numList[0] <= numList[1] and numList[0] < num:
                    numList[0] = num
                elif numList[1] <= numList[0] and numList[1] < num:
                    numList[1] = num

                res = max(res, numList[0] + numList[1])
        return res

            