class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Time: O(n), Space: O(1)
        diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
        return len(diffs) == 0 or (len(diffs) == 2 and diffs[0] == diffs[1][::-1])
