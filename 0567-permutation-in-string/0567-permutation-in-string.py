class Solution:
   

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for i in range(len(s1)):
            s1_map[s1[i]] += 1
            s2_map[s2[i]] += 1
        
        def isMatch():
            for k, v in s2_map.items():
                if s1_map[k] != v:
                    return False
            
            return True

        for i in range(len(s2) - len(s1)):
            if isMatch():
                return True
            
            s2_map[s2[i]] -= 1
            s2_map[s2[i + len(s1)]] += 1

        return False

        