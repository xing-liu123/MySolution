from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)

        for task in tasks:
            task_count[task] += 1
        
        max_heap = [(-count, task) for task, count in task_count.items()]
        heapq.heapify(max_heap)

        cooldown_queue = deque()

        time = 0

        while max_heap or cooldown_queue:
            time += 1

            if cooldown_queue and cooldown_queue[0][0] == time:
                _, task, count = cooldown_queue.popleft()
                heapq.heappush(max_heap, (count, task))
            
            if max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    cooldown_queue.append((time + n + 1, task, count))


        return time