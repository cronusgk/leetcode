from utils.nodes import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while (fast and fast.next):
            if (slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next
        return False