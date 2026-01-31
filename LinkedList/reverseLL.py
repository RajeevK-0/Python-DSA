# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        temp = head
        while temp is not None:
            nextNode = temp.next
            temp.next = newHead
            newHead = temp
            temp = nextNode
        return newHead