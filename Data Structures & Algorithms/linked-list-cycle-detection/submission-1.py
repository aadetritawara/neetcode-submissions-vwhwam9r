# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's tortoise and hare
        # space: O(1), time: O(n)

        slow, fast = head, head

        # need to make sure fast.next also not null because we're shifting by 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
