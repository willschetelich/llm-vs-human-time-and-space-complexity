import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Time: O(1), Space: O(1)
        rounds = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets) / math.log(rounds + 1))
