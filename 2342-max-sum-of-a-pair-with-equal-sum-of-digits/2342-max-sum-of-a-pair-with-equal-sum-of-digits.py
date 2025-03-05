class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitSums = defaultdict(lambda: [0, 0])  # Store top 2 largest numbers
        res = -1

        for num in nums:
            digitSum = sum(int(d) for d in str(num))  # Compute digit sum
            max1, max2 = digitSums[digitSum]

            # Update top two largest numbers in this digit sum group
            if num > max1:
                max1, max2 = num, max1  # Shift down
            elif num > max2:
                max2 = num  # Replace second largest

            digitSums[digitSum] = [max1, max2]  # Store updated values
            
            # Compute max sum if we have at least two numbers
            if max2 > 0:
                res = max(res, max1 + max2)

        return res

            