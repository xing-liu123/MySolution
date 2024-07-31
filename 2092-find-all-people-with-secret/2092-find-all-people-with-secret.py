from collections import deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        share_times = [sys.maxsize] * n
        share_times[0] = 0
        share_times[firstPerson] = 0

        meeting_times = defaultdict(list)

        for p1, p2, t in meetings:
            meeting_times[p1].append((p2, t))
            meeting_times[p2].append((p1, t))
            
        queue = deque([0, firstPerson])

        while queue:
            person = queue.popleft()

            for next_person, time in meeting_times[person]:
            
                if share_times[person] <= time < share_times[next_person]:
                    share_times[next_person] = time
                    queue.append(next_person)

        return [i for i in range(n) if share_times[i] != sys.maxsize]
