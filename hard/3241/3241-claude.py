from typing import List
from collections import defaultdict, deque

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        # Time: O(n), Space: O(n) rerooting DP on tree
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # down[node] = max dist going into subtree, adjusted for parity
        down = [0] * n
        down2 = [0] * n
        down_child = [-1] * n

        def dfs1(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs1(nei, node)
                parity = 1 if nei % 2 == 1 else 0
                d = down[nei] + 1 + parity
                if d > down[node]:
                    down2[node] = down[node]
                    down[node] = d
                    down_child[node] = nei
                elif d > down2[node]:
                    down2[node] = d

        dfs1(0, -1)
        result = [0] * n
        up = [0] * n

        def dfs2(node, parent):
            result[node] = max(down[node], up[node])
            for nei in graph[node]:
                if nei == parent:
                    continue
                parity = 1 if nei % 2 == 1 else 0
                best_from_node = down2[node] if down_child[node] == nei else down[node]
                up[nei] = max(up[node], best_from_node) + 1 + parity
                dfs2(nei, node)

        dfs2(0, -1)
        return result
