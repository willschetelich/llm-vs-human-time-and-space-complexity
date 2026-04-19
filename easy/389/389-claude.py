class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(n), Space: O(1)
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)
