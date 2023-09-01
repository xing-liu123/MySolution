class Solution:
    @staticmethod
    def match(l1: list, l2: list) -> bool:
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
            
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1list = [0] * 26
        s2list = [0] * 26

        for i in range(len(s1)):
            s1list[ord(s1[i]) - ord('a')] += 1
            s2list[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1)):
            if self.match(s1list, s2list):
                return True;
            else:
                s2list[ord(s2[i]) - ord('a')] -= 1
                s2list[ord(s2[i + len(s1)]) - ord('a')] += 1
        
        return self.match(s1list, s2list)