
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)
        
        for word in words:
            start = s.find(word)
            
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                
                start = s.find(word, start + 1)
        
        left = "<b>"
        right = "</b>"
        
        ans = []
        
        for i in range(len(s)):
            if bold[i]:
                if i == 0 or not bold[i - 1]:
                    ans.append(left)
                
                ans.append(s[i])
                
                if i == len(s) - 1:
                    ans.append(right)
                    
            else:
                if i > 0 and bold[i - 1]:
                    ans.append(right)
                
                ans.append(s[i])
                
        return ''.join(ans)