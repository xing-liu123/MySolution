# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         # self.is_end = False
        

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.prefix = None
    
#     def insert(self, word):
#         curr = self.root
#         currPrefix = ""

#         for c in word:
#             if not c in curr.children:
#                 curr.children[c] = TrieNode()

#             if len(curr.children) > 1:
#                 break
#             currPrefix += c
#             curr = curr.children[c]

#         if not self.prefix or len(currPrefix) < len(self.prefix):
#             self.prefix = currPrefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # root = Trie()
        
        # for s in strs:
        #     if s == "":
        #         return ""
        #     root.insert(s)

        # return root.prefix

        for i in range(len(strs[0])):
            c = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or word[i] != c:
                    if i == 0:
                        return ""
                    else:
                        return strs[0][:i]


        return strs[0]
            




        
            

