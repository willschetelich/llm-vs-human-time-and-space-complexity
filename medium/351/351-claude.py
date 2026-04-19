class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Time: O(n! * n^2), Space: O(n)
        skip = [[0]*10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = 5
        skip[4][6] = skip[6][4] = 5

        def dfs(curr, visited, remaining):
            if remaining < 0:
                return 0
            count = 1 if remaining >= 0 else 0
            for nxt in range(1, 10):
                mid = skip[curr][nxt]
                if nxt not in visited and (mid == 0 or mid in visited):
                    visited.add(nxt)
                    count += dfs(nxt, visited, remaining - 1)
                    visited.remove(nxt)
            return count

        total = 0
        for length in range(m, n+1):
            # By symmetry: 1,3,7,9 same; 2,4,6,8 same; 5 unique
            visited = {1}
            total += dfs(1, visited, length - 2) * 4
            visited = {2}
            total += dfs(2, visited, length - 2) * 4
            visited = {5}
            total += dfs(5, visited, length - 2)
        return total
