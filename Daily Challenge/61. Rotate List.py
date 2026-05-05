# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        last.next = head
        rotations = k%length
        skip = length - rotations

        newlast = head

        for i in range(skip-1):
            newlast = newlast.next

        head = newlast.next
        newlast.next = None

        return head

