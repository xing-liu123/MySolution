class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # res = []

        # if len(s) < 10:
        #     return res

        # string_set = {}

        # curr_string = s[0 : 10]
        # string_set[curr_string] = 1

        # for i in range(10, len(s)):
        #     curr_string = curr_string[1:] + s[i]

        #     if curr_string in string_set:
        #         if string_set[curr_string] == 1:
        #             res.append(curr_string)
        #             string_set[curr_string] = 2
        #     else:
        #          string_set[curr_string] = 1
        
        # return res
        
        if len(s) < 0:
            return []

        dna_set = set()
        res = set()

        curr = s[:10]
        dna_set.add(curr)

        for i in range(10, len(s)):
            curr = curr[1:] + s[i]

            if curr in dna_set:
                res.add(curr)
            else:
                dna_set.add(curr)
        
        return list(res)
        


