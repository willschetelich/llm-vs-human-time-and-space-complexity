class Solution:
    def countSegments(self, s: str) -> int:
        # Time: O(n), Space: O(1)
        return len(s.split())
