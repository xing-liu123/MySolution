class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(list(s)))

            strings[sorted_str].append(s)

        return [group for group in strings.values()]



