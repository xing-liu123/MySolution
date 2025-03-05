class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            x = str(x)
            y = str(y)
            if int(x + y) > int(y + x):
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        res = ''.join(str(num) for num in nums)

        return res[0] if res[0] == "0" else res