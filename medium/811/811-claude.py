from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Time: O(n*L), Space: O(n*L) where L is avg domain length
        count = defaultdict(int)
        for entry in cpdomains:
            cnt, domain = entry.split()
            cnt = int(cnt)
            parts = domain.split('.')
            for i in range(len(parts)):
                count['.'.join(parts[i:])] += cnt
        return [f"{v} {k}" for k, v in count.items()]
