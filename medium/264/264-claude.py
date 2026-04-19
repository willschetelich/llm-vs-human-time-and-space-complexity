class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Time: O(n), Space: O(n)
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            next2, next3, next5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            ugly[i] = min(next2, next3, next5)
            if ugly[i] == next2: i2 += 1
            if ugly[i] == next3: i3 += 1
            if ugly[i] == next5: i5 += 1
        return ugly[-1]
