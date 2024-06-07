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
#                 else:
#                     i += 1
#                     j += 1
#             elif i == 0:
#                 j += 1
#             else:
#                 i = table[i - 1]             
        
#         return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        lastOccurenceTable = self.buildLastOccurenceTable(needle)
        
        i = 0
        
        while i <= len(haystack) - len(needle):
            j = len(needle) - 1
            
            while j >= 0 and haystack[i + j] == needle[j]:
                j -= 1
            
            if j == -1:
                return i
            else:
                shift = lastOccurenceTable.get(haystack[i + j], -1)
                
                if shift < j:
                    i = i + j - shift
                else:
                    i += 1
                    
        return -1
        
    def buildLastOccurenceTable(self, needle: str) -> List[str]:
        lastOccurenceTable = {}
        
        for i in range(len(needle)):
            lastOccurenceTable[needle[i]] = i
        
        return lastOccurenceTable
        
        
        
                
        
        