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
    # temp = self.head
        # newHead =  self.head
        # if temp is None or temp.next is None:
        #         return temp
        # while temp.next.next is not None:
        #     t = temp.next.next
        #     temp.next.next = temp
        #     temp = temp.next
        # self.head = temp.next.next