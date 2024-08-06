class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
            
        root = dict()
        size = dict()

        num_map = defaultdict(lambda: 0)

        for num in nums:
            num_map[num] += 1
        

        def find(u):
            if root[u] != u:
                root[u] = find(root[u])
            return root[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                root[root_v] = root_u
                size[root_u] += size[root_v]
        
        def gcd(u, v) -> bool:
            while v != 0:
                u, v = v, u % v
            
            return u

        if len(num_map) == 1:
            if nums[0] != 1:
                return True
            else:
                return False

        
        for num in num_map.keys():
            root[num] = num
            size[num] = num_map[num]
        
        for num1 in num_map.keys():
            for num2 in num_map.keys():
                if num1 != num2 and gcd(num1, num2) > 1:
                    union(num1, num2)
        
        return max(size.values()) == n