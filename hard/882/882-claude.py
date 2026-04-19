from typing import List
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Time: O((E + n) log n), Space: O(E + n)
        graph = [[] for _ in range(n)]
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        dist = {0: maxMoves}
        heap = [(-maxMoves, 0)]
        while heap:
            moves, node = heapq.heappop(heap)
            moves = -moves
            if moves < dist.get(node, 0):
                continue
            for nei, cnt in graph[node]:
                moves_to_nei = moves - cnt - 1
                if moves_to_nei > dist.get(nei, -1):
                    dist[nei] = moves_to_nei
                    heapq.heappush(heap, (-moves_to_nei, nei))

        result = len(dist)
        for u, v, cnt in edges:
            reached_from_u = max(0, dist.get(u, -1))
            reached_from_v = max(0, dist.get(v, -1))
            result += min(cnt, reached_from_u + reached_from_v)
        return result
