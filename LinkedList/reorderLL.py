# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def reorder(self,head,res):
    #     if head == None:
    #         return res
    #     res.val = head.val
    #     t = head
    #     head = head.next
    #     while head.next is not None:
    #         t = t.next
    #         head = head.next
    #     res.next = t
    #     head = None
    #     self.reorder(head,res) 
        # return res
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head , head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        second = s.next
        s.next = None
        new = None
        while second :
            temp = second.next
            second.next = new
            new = second
            second = temp
        
        first, second = head, new
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        # l , r = ListNode() , ListNode()
        # t = head
        # lh = t
        # while t != s:
        #     l = t
        #     t = t.next
        #     l = l.next
        # while t and t.next:
        #     if r is None:
        #         r = t
        #     r.next = r
        #     r = t
        #     t = t.next
        # k = lh
        # print(l.val)
        # print(r.val)
        # while k is not None:
        #     head = k
        #     if r:
        #         head.next = r
        #         r = r.next
        #     k = k.next
        # res  = ListNode()
        # return self.reorder(head,res)