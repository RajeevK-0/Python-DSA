# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    # def trav(self,root,l):
    #     if root is None:
    #         l.append(None)
    #     else:
    #         l.append(root.val)
    #         self.trav(root.left,l)
    #         self.trav(root.right,l)
    #     return l
    def sameTree(self,root,subroot):
        if root is None and subroot is None:
            return True
        if root is None or subroot is None:
            return False
        if root and subroot and root.val == subroot.val:
            if self.sameTree(root.left,subroot.left) and self.sameTree(root.right,subroot.right):
                return True
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        if subRoot is None:
            return True    
        if root and subRoot and root.val == subRoot.val:
            if self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
