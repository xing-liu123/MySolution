class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence = defaultdict(int)

        for i in range(len(s)):
            lastOccurence[s[i]] = i

        res = []

        left = 0
        right = lastOccurence[s[left]]

        for i in range(len(s)):
            if i == right:
                res.append(right - left + 1)
                left = right + 1
                if left <= len(s) - 1:
                    right = lastOccurence[s[left]]
            else:
                right = max(right, lastOccurence[s[i]])
                

        return res
        
