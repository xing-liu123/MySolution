class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index_map = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.index_map[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.index_map[word1]
        list2 = self.index_map[word2]

        idx1, idx2 = 0, 0

        min_diff = sys.maxsize

        while idx1 < len(list1) and idx2 < len(list2):
            curr_diff = abs(list1[idx1] - list2[idx2])

            min_diff = min(min_diff, curr_diff)

            if list1[idx1] < list2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        return min_diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)