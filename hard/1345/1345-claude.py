from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Time: O(n), Space: O(n)
        n = len(arr)
        if n == 1:
            return 0
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        visited = {0}
        queue = deque([(0, 0)])
        while queue:
            idx, steps = queue.popleft()
            for nxt in [idx-1, idx+1] + graph[arr[idx]]:
                if nxt == n - 1:
                    return steps + 1
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps+1))
            graph[arr[idx]] = []
        return -1
