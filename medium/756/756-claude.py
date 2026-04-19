from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Time: O(7^n) bounded by allowed combos, Space: O(n)
        mapping = defaultdict(list)
        for triple in allowed:
            mapping[triple[:2]].append(triple[2])

        def build(row):
            if len(row) == 1:
                return True
            next_rows = ['']
            for i in range(len(row) - 1):
                pair = row[i:i+2]
                tops = mapping[pair]
                if not tops:
                    return False
                next_rows = [prev + t for prev in next_rows for t in tops]
            return any(build(nr) for nr in next_rows)

        return build(bottom)
