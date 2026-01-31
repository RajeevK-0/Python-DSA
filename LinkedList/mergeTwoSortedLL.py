# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        tail = None
        # if list1 is None and list2 is None:
        #     return list1
        if list1 is None :
            return list2
        if list2 is None :
            return list1
        temp1 = list1
        temp2 = list2
        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                if newHead == None:
                    newHead,tail = temp1,temp1

                else:
                    tail.next = temp1
                    tail = temp1
                temp1 = temp1.next
            else:
                if newHead == None:
                    newHead,tail = temp2,temp2
                else:
                    tail.next = temp2
                    tail = temp2
                temp2 = temp2.next
        tail.next = temp1 or temp2
        return newHead          