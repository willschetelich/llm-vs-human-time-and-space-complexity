from typing import List

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # Time: O(log n), Space: O(log n)
        parts = list(map(int, ip.split('.')))
        start = (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]
        result = []
        while n > 0:
            lsb = start & (-start) if start != 0 else 1 << 31
            while lsb > n:
                lsb >>= 1
            prefix = 32 - lsb.bit_length() + 1
            ip_str = '.'.join(str((start >> (24 - 8*i)) & 0xFF) for i in range(4))
            result.append(f"{ip_str}/{prefix}")
            start += lsb
            n -= lsb
        return result
