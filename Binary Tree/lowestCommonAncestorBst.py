# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def rsearch(self,root,n):
    #     if root is None:
    #         return False
    #     if root.val == n.val:
    #         return True
    #     return (self.rsearch(root.left,n) or
    #             self.rsearch(root.right,n))
    # def search(self,root,n):
    #     return self.rsearch(root,n)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = root
        while temp:
            if temp.val < p.val and temp.val < q.val:
                temp = temp.right
            if temp.val > p.val and temp.val > q.val:
                temp = temp.left
            else:
                return temp
    # class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # Start at the root and move down the tree
    #     curr = root
        
    #     while curr:
    #         # If both p and q are greater than curr, move to the right child
    #         if p.val > curr.val and q.val > curr.val:
    #             curr = curr.right
    #         # If both p and q are smaller than curr, move to the left child
    #         elif p.val < curr.val and q.val < curr.val:
    #             curr = curr.left
    #         else:
    #             # We found the split point! 
    #             # (One is left, one is right, or curr is p or q)
    #             return curr
        # if root is None:
        #     return root
        # if self.search(root,p) and self.search(root,q):
        #     left =  self.lowestCommonAncestor(root.left,p,q)
        #     right = self.lowestCommonAncestor(root.right,p,q)
        #     return left or right or root
        # return TreeNode()