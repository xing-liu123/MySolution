class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_num = {}

        for idx, num in enumerate(nums):
            self.index_num[idx] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        if len(self.index_num) <= len(vec.index_num):
            for key, val in self.index_num.items():
                if key in vec.index_num:
                    res += val * vec.index_num[key]

        else:
            for key, val in vec.index_num.items():
                if key in self.index_num:
                    res += val * self.index_num[key]

        return res

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)