from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n), Space: O(1) (alphabet size is fixed)
        return Counter(s) == Counter(t)
