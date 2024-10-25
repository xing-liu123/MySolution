class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = defaultdict(int)

        for task in tasks:
            taskCounts[task] += 1

        maxHeap = [(-count, -n, task) for task, count in taskCounts.items()]
        heapq.heapify(maxHeap)
        
        currTime = 0

        taskNotReady = []
        while maxHeap:
            currTime += 1

            while maxHeap and currTime - maxHeap[0][1] < n + 1:
                taskNotReady.append(heapq.heappop(maxHeap))

            if maxHeap:
                count, lastExecuteTime, task = heapq.heappop(maxHeap)
                count += 1
                if count < 0:
                    heapq.heappush(maxHeap, (count, currTime, task))

            if taskNotReady:
                maxHeap.extend(taskNotReady)
                taskNotReady = []
                heapq.heapify(maxHeap)

        return currTime



        