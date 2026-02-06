# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invTree(self,root):
        if root is not None:
            right = self.invTree(root.right)
            left = self.invTree(root.left)
            root.right = left
            root.left = right
            # root.right = self.invTree(root.left)
            # root.left = self.invTree(t)
        return root  
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invTree(root)