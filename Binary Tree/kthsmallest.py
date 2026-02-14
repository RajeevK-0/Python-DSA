# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    c = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.result  = None
        def trav(node):
            if node is None or self.result is not None:
                return
            trav(node.left)
            self.count -= 1
            if self.count == 0:
                self.result = node.val
                return
            trav(node.right)
        trav(root)
        return self.result

        # return self.trav(root,k).kelement
        # res =[]
        # self.inOrd(root,k,res)
        # return res[k-1] 