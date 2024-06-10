class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [word for word in s.strip().split(' ') if word]
        
        arr.reverse()
        
        return ' '.join(arr)