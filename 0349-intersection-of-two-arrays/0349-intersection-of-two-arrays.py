class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet1 = set()
        numSet2 = set()

        for num in nums1:
            numSet1.add(num)

        for num in nums2:
            numSet2.add(num)

        return list(numSet1 & numSet2)