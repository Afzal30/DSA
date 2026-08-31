# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]

        prev = head
        curr = prev.next
        nxt = curr.next
        pos = 1



        first_critical = -1
        prev_critical = -1
        max_distance = -1
        min_distance = float('inf')

        while nxt:

            if (curr.val>prev.val and curr.val>nxt.val) or (curr.val<prev.val and curr.val<nxt.val):
                if first_critical==-1:
                    first_critical = pos

                else:
                    min_distance = min(min_distance,pos - prev_critical)
                    max_distance = pos - first_critical

                prev_critical = pos

            prev = curr
            curr = nxt
            nxt = nxt.next
            pos +=1

        if max_distance == -1:
            return [-1,-1]
        else:
            return [min_distance,max_distance]

        

            

        
