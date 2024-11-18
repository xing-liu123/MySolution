class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        
        for val, idx in people:
            res.insert(idx, [val, idx])
        
        return res