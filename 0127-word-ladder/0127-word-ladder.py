from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word_set = set(wordList)

        # if not endWord in word_set:
        #     return 0

        # queue = deque([beginWord])

        # length = 1

        # while queue:
        #     size = len(queue)
        #     length += 1

        #     for _ in range(size):
        #         word = queue.popleft()

        #         for i in range(len(word)):
        #             for j in range(26):
        #                 next_word = word[:i] + chr(ord('a') + j) + word[i + 1:]

        #                 if next_word in word_set:
        #                     if next_word == endWord:
        #                         return length

        #                     queue.append(next_word)
        #                     word_set.remove(next_word)
        # return 0

        from collections import deque

        wordSet = set(wordList)

        if not endWord in wordSet:
            return 0

        queue = deque([beginWord])
        count = 1

        while queue:
            count += 1
            size = len(queue)

            for _ in range(size):
                word = queue.popleft()

                for idx in range(len(word)):
                    for c in ascii_lowercase:
                        newWord = word[:idx] + c + word[idx + 1:]

                        if newWord == endWord:
                            return count

                        if newWord in wordSet:
                            queue.append(newWord)
                            wordSet.remove(newWord)
        
        return 0


        # from collections import deque
        
        # wordSet = set(wordList)

        # if not endWord in wordSet:
        #     return 0

        # queue = deque([beginWord])
        # count = 0

        # while queue:
        #     size = len(queue)
        #     count += 1

        #     for _ in range(size):
        #         word = queue.popleft()

        #         for i in range(len(word)):
        #             for c in string.ascii_lowercase:
        #                 nextWord = word[:i] + c + word[i + 1:]

        #                 if nextWord in wordSet:
        #                     if nextWord == endWord:
        #                         return count + 1

        #                     queue.append(nextWord)
        #                     wordSet.remove(nextWord)

        # return 0


        

            
