class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings_map = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(list(word)))

            strings_map[sorted_word].append(word)

        return [string_list for string_list in strings_map.values()]