from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Time: O(m*n), Space: O(m*n)
        orig = image[sr][sc]
        if orig == color:
            return image
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == orig:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        return image
