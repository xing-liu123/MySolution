class Visit:
    def __init__(self, time, web):
        self.time = time
        self.web = web

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userVisitedLists = defaultdict(list)

        for user, time, web in zip(username, timestamp, website):
            userVisitedLists[user].append((time, web))

        patternCount = defaultdict(int)

        for visitList in userVisitedLists.values():
            if len(visitList) >= 3:
                visitList.sort()
                uniquePatterns = set()
                for i in range(len(visitList) - 2):
                    _, web1 = visitList[i]
                    _, web2 = visitList[i + 1]
                    _, web3 = visitList[i + 2]
                    uniquePatterns.add((web1, web2, web3))

                for uniquePattern in uniquePatterns:
                    patternCount[uniquePattern] += 1
        
        maxCount = max(patternCount.values())

        return sorted(triple for triple, count in patternCount.items() if count == maxCount)[0]







        
