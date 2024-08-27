class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        goal = len(nums) // 3

        return [key for key, val in counts.items() if val > goal]