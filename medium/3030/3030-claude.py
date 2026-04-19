from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(image), len(image[0])
        region_id = [[-1]*n for _ in range(m)]
        regions = []

        def valid_region(r, c, dr, dc, size):
            for i in range(size):
                for j in range(size - 1):
                    if dr == 0:
                        if abs(image[r+i][c+j] - image[r+i][c+j+1]) > threshold:
                            return False
                    else:
                        if abs(image[r+j][c+i] - image[r+j+1][c+i]) > threshold:
                            return False
            return True

        for r in range(m - 2):
            for c in range(n - 2):
                ok = True
                for i in range(3):
                    for j in range(2):
                        if abs(image[r+i][c+j] - image[r+i][c+j+1]) > threshold:
                            ok = False; break
                        if abs(image[r+j][c+i] - image[r+j+1][c+i]) > threshold:
                            ok = False; break
                    if not ok:
                        break
                if ok:
                    total = sum(image[r+i][c+j] for i in range(3) for j in range(3))
                    avg = total // 9
                    for i in range(3):
                        for j in range(3):
                            if region_id[r+i][c+j] == -1:
                                region_id[r+i][c+j] = avg
                            else:
                                region_id[r+i][c+j] = (region_id[r+i][c+j] + avg) // 2

        result = [[image[r][c] if region_id[r][c] == -1 else region_id[r][c] for c in range(n)] for r in range(m)]
        return result
