# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # space: O(1), time: O(n)
        
        # find middle of linked list using 2 pointers
        slow, fast = head, head.next

        # when fast reaches the end, slow will be at midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # disconnect two halves
        second_half = slow.next
        prev = slow.next = None

        # reverse second half
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp

        # merge both halves
        first, second = head, prev
        # keep going until one of the two halves is null but since only second can be smaller can just check it
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2