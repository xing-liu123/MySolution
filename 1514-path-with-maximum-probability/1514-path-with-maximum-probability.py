class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        max_heap = [(-1, start_node)]

        p_of_node = defaultdict(lambda: 0)

        p_of_node[start_node] = 1.0

        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob

            for next_node, prob in graph[node]:
                next_prob = curr_prob * prob
                if next_prob > p_of_node[next_node]:
                    p_of_node[next_node] = next_prob 
                    heapq.heappush(max_heap, (-next_prob, next_node))

        return 0


