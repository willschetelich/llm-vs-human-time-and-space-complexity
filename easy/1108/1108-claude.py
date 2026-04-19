class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Time: O(n), Space: O(n)
        return address.replace('.', '[.]')
