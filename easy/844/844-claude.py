class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time: O(n+m), Space: O(1)
        def process(string):
            skip = 0
            result = []
            for c in reversed(string):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    result.append(c)
            return result
        return process(s) == process(t)
