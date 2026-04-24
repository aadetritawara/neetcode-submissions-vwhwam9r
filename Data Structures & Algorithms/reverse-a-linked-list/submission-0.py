# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            n = head.next
            prev = head
            head.next = None
        while head and n:
            head = n
            n = head.next
            head.next = prev
            prev = head

        return head