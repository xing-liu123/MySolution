class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        fruit_counts = {}

        left = 0

        for right, f in enumerate(fruits):
            if f not in fruit_counts:
                fruit_counts[f] = 1
            else:
                fruit_counts[f] += 1

            while len(fruit_counts) > 2:
                fruit_counts[fruits[left]] -= 1

                if fruit_counts[fruits[left]] == 0:
                    del fruit_counts[fruits[left]]
                
                left += 1

            res = max(res, right - left + 1)

        return res
                
            

