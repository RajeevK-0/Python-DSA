# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If the helper returns anything other than -1, it's balanced
        return self.check_height(root) != -1

    def check_height(self, root):
        if not root:
            return 0
        
        # Check left subtree
        left_height = self.check_height(root.left)
        if left_height == -1: return -1
        
        # Check right subtree
        right_height = self.check_height(root.right)
        if right_height == -1: return -1
        
        # If the difference is > 1, this node is unbalanced
        if abs(left_height - right_height) > 1:
            return -1
            
        # Otherwise, return the actual height to the parent
        return 1 + max(left_height, right_height)