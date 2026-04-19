from typing import List

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Time: O(V+E), Space: O(V+E)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        # 0=unvisited, 1=visiting, 2=done-good, 3=done-bad
        state = [0] * n
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            if not graph[node]:
                if node == destination:
                    state[node] = 2
                    return True
                state[node] = 3
                return False
            state[node] = 1
            for nxt in graph[node]:
                if state[nxt] == 1 or not dfs(nxt):
                    state[node] = 3
                    return False
            state[node] = 2
            return True
        return dfs(source)
