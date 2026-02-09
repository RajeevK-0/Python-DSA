# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trav(self,root,l):
        if root is None:
            l.append(None)
        else:
            l.append(root.val)
            self.trav(root.left,l)
            self.trav(root.right,l)
        return l
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.trav(p,[]) == self.trav(q,[])
        # if p is None and q is None:
        #     return True
        # if p is None:
        #     return False
        # if q is None:
        #     return False
        # l1 = []
        # l2 = []
        # return self.trav(p,l1) == self.trav(q,l2)