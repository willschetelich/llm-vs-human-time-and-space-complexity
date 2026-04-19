class Solution:
    def countCollisions(self, directions: str) -> int:
        # Time: O(n), Space: O(1)
        # strip leading L and trailing R (they never collide)
        s = directions.lstrip('L').rstrip('R')
        return len(s) - s.count('S')
