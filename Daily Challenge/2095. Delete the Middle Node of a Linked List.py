# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head :
            return head

        if not head.next:
            return None

        if not head.next.next:
            head.next = None

        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev=slow
            slow = slow.next
            fast = fast.next.next

        #print(slow)
        
        prev.next = slow.next

        return head
        
