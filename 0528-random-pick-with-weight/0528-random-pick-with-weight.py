class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        prefix = 0

        for num in w:
            prefix += num
            self.w.append(prefix)

        self.totalSum = prefix

    def pickIndex(self) -> int:
        choice = random.randint(1, self.totalSum)
        return bisect.bisect_left(self.w, choice)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()