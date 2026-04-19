from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Time: O(n * 2^n) where n=non-zero balances, Space: O(n)
        balance = defaultdict(int)
        for u, v, amount in transactions:
            balance[u] -= amount
            balance[v] += amount
        debts = [v for v in balance.values() if v != 0]

        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            result = float('inf')
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    result = min(result, 1 + dfs(start + 1))
                    debts[i] -= debts[start]
            return result

        return dfs(0)
