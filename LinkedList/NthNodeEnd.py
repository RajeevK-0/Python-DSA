# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0 
        temp = head
        while temp is not None:
            l+=1
            temp = temp.next
        t = l-n
        if t == 0:
            return head.next
        point = head
        while t != 1:
            point = point.next
            t-=1
        point.next = point.next.next
        return head