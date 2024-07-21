class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_map = dict()

        for i in range(len(nums1)):
            nums_map[nums1[i]] = i

        stack = []

        res = [-1] * len(nums1)

        stack.append(0)

        for i in range(1, len(nums2)):
            if nums2[stack[-1]] > nums2[i]:
                stack.append(i)
            elif nums2[stack[-1]] < nums2[i]:
                while stack and nums2[stack[-1]] < nums2[i]:
                    idx = stack.pop()
                    if nums2[idx] in nums_map:
                        res[nums_map[nums2[idx]]] = nums2[i]
                
                stack.append(i)
        
        return res
