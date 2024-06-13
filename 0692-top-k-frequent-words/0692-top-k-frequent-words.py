class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = {}
        
        for word in words:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1
        
        return [item[0] for item in sorted(map.items(), key=lambda item: (-item[1], item[0]))[:k]]