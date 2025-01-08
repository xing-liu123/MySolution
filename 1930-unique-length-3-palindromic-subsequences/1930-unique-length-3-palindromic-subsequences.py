class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_indices = defaultdict(list)

        for idx, char in enumerate(s):
            char_indices[char].append(idx)

        count = 0

        for indice_list in char_indices.values():
            if len(indice_list) > 1:
                left, right = indice_list[0], indice_list[-1]
                char_set = set()

                for i in range(left + 1, right):
                    char_set.add(s[i])

                count += len(char_set)

        return count

        

        