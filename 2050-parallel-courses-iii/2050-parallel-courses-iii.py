from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        degrees = [0] * (n + 1)
        completion_times = [0] * (n + 1)

        graph = defaultdict(list)

        for u, v in relations:
            degrees[v] += 1
            graph[u].append(v)

        queue = deque()

        for i in range(1, n + 1):
            if degrees[i] == 0:
                queue.append(i)
                completion_times[i] = time[i - 1]

        while queue:
           course = queue.popleft()

           for next_course in graph[course]:
                degrees[next_course] -= 1
                completion_times[next_course] = max(completion_times[next_course], completion_times[course] + time[next_course - 1])
                if degrees[next_course] == 0:
                    queue.append(next_course)             

        return max(completion_times)


        

        


        