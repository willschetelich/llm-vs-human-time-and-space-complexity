class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Time: O(n), Space: O(1)
        bulls = sum(s == g for s, g in zip(secret, guess))
        s_count = [0] * 10
        g_count = [0] * 10
        for s, g in zip(secret, guess):
            if s != g:
                s_count[int(s)] += 1
                g_count[int(g)] += 1
        cows = sum(min(s_count[i], g_count[i]) for i in range(10))
        return f"{bulls}A{cows}B"
