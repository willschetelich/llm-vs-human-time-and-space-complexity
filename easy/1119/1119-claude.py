class Solution:
    def removeVowels(self, s: str) -> str:
        # Time: O(n), Space: O(n)
        vowels = set('aeiou')
        return ''.join(c for c in s if c not in vowels)
