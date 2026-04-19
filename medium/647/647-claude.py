class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(n^2), Space: O(1)
        count = 0
        for center in range(2 * len(s) - 1):
            lo = center // 2
            hi = lo + center % 2
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
        return count
