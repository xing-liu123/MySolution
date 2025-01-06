class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}
        char_set = set()

        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in char_set:
                    return False

                char_map[s[i]] = t[i]
                char_set.add(t[i])
                
            elif char_map[s[i]] != t[i]:
                return False

        return True
 

        