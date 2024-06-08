class Solution:
#     def buildFailureTable(self, needle: str) -> List[str]:
#         table = [0] * len(needle)
        
#         i, j = 0, 1
        
#         while j < len(needle):
#             if needle[i] == needle[j]:
#                 table[j] = i + 1
#                 i += 1
#                 j += 1
#             elif i == 0:
#                 j += 1
#             else:
#                 i = table[i - 1]
        
#         return table
    
#     def strStr(self, haystack: str, needle: str) -> int:
#         if len(needle) > len(haystack):
#             return -1
        
#         table = self.buildFailureTable(needle)
        
#         i, j = 0, 0
        
#         while j < len(haystack):
#             if needle[i] == haystack[j]:
#                 if i == len(needle) - 1:
#                     return j - i
#                 i += 1
#                 j += 1
#             elif i == 0:
#                 j += 1
#             else:
#                 i = table[i - 1]
        
#         return -1
        
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        table = self.buildLastOccurenceTable(needle)
        
        j = 0
        
        while j <= len(haystack) - len(needle):
            i = len(needle) - 1
            
            while i >= 0 and needle[i] == haystack[j + i]:
                i -= 1
            
            if i == -1:
                return j
            else:
                shift = table.get(haystack[j + i], -1)
                
                if shift < i:
                    j = i + j - shift
                else:
                    j = j + 1
        
        return -1
        
    def buildLastOccurenceTable(self, needle: str) -> List[str]:
        lastOccurenceTable = {}
        
        for i in range(len(needle)):
            lastOccurenceTable[needle[i]] = i
        
        return lastOccurenceTable
        
        
        
                
        
        