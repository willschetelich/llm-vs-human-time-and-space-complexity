from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Time: O(n log n), Space: O(n)
        heap = []
        fuel = startFuel
        stops = 0
        prev = 0
        for pos, cap in stations + [[target, 0]]:
            fuel -= pos - prev
            while heap and fuel < 0:
                fuel += -heapq.heappop(heap)
                stops += 1
            if fuel < 0:
                return -1
            heapq.heappush(heap, -cap)
            prev = pos
        return stops
