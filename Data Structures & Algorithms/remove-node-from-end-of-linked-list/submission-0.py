# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        # add all nodes to an array
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        # find node index to remove
        to_remove = len(nodes) - n

        # remove and reorder nodes
        if len(nodes) == 1:
            return None
        elif to_remove == 0: # first element
            nodes[to_remove] = nodes[to_remove].next
        elif to_remove == len(nodes) - 1: # last element
            nodes[to_remove - 1].next = None
        else:
            nodes[to_remove - 1].next = nodes[to_remove + 1]

        return nodes[0]
