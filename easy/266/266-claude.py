from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Time: O(n), Space: O(1) (alphabet size fixed)
        return sum(v % 2 for v in Counter(s).values()) <= 1
