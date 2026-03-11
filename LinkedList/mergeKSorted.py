# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self,node,res):
        n = ListNode(node.val)
        dummy = ListNode(0)
        dummy.next = res
        prev = dummy
        while prev.next and prev.next.val < node.val:
            prev = prev.next
        n.next = prev.next
        prev.next = n
        return dummy.next      
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for i in lists:
            t = i
            while t: 
                res = self.insert(t,res)
                t = t.next
        return res