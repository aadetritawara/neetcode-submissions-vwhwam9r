# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # space: O(1), time: O(n)

        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right n steps ahead of start
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move both pointers by 1 until right reaches the end
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next

