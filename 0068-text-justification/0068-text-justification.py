class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        start = 0

        while start < len(words):
            currLength = len(words[start])
            idx = start + 1

            while idx < len(words) and currLength + (idx - start) + len(words[idx]) <= maxWidth:
                currLength += len(words[idx])
                idx += 1

            wordCount = idx - start
            space = (maxWidth - currLength) // (wordCount - 1) if wordCount != 1 else maxWidth - currLength
            remain = (maxWidth - currLength) % (wordCount - 1) if wordCount != 1 else 0

            line = words[start]
            if idx == len(words):
                for i in range(start + 1, idx):
                    line += " "
                    line += words[i]
                
                line += " " * (maxWidth - currLength - (wordCount - 1))
            elif wordCount == 1:
                line += " "*(maxWidth - currLength)
            else:
                for i in range(start + 1, idx):
                    line += " "*space
                    if i - start <= remain:
                        line += " "
                    line += words[i]
            
            start = idx

            res.append(line)
        return res

            
