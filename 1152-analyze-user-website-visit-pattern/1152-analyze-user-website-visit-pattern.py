class Visit:
    def __init__(self, time, web):
        self.time = time
        self.web = web

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visit = defaultdict(list)

        for user, time, web in zip(username, timestamp, website):
            user_visit[user].append((time, web))

        pattern_count = Counter()

        for visit_list in user_visit.values():
            visit_list.sort()
            pattern_set = set()

            n = len(visit_list)

            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = (visit_list[i][1], visit_list[j][1], visit_list[k][1])
                        if not pattern in pattern_set:
                            pattern_set.add(pattern)
                            pattern_count[pattern] += 1
            
        sorted_pattern = sorted(pattern_count.items(), key=lambda x: (-x[1], x[0]))

        return list(sorted_pattern[0][0])

                

        

        
