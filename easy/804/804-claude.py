from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Time: O(n*L), Space: O(n*L) where L is avg word length
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({'.'.join(morse[ord(c)-ord('a')] for c in w) for w in words})
