class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x1, x2):
            if str(x1) + str(x2) > str(x2) + str(x1):
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        res = ""

        for num in nums:
            res += str(num)

        
        return res if res[0] != "0" else "0"