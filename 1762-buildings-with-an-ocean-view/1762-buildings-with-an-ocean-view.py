class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        queue = []

        for i, h in enumerate(heights):
            while queue and h >= heights[queue[-1]]:
                queue.pop()

            queue.append(i)

        return queue