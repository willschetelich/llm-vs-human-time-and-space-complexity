from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Time: O(n), Space: O(1)
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = self._get_kth(prev_group, k)
            if not kth:
                break
            group_next = kth.next
            prev, curr = kth.next, prev_group.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp
        return dummy.next

    def _get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
