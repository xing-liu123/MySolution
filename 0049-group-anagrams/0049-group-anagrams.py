class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def getSortedStr(s):
            chars = list(s)

            return ''.join(sorted(chars)) 

        for s in strs:
            groups[getSortedStr(s)].append(s)

        return [l for l in groups.values()]


