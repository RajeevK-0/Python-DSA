# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    class NodeInfo:
        def __init__(self,minimum = float('inf'),maximum = float('-inf'),valid = True):
            self.minimum = minimum
            self.maximum = maximum
            self.valid = valid
    def isvalid(self,root):
        if root == None:
            return self.NodeInfo()
        left = self.isvalid(root.left)
        right = self.isvalid(root.right)
        if (root.val>left.maximum and root.val<right.minimum and left.valid and right.valid):
            return self.NodeInfo(minimum = min(left.minimum,right.minimum,root.val),maximum = max(root.val,left.maximum,right.maximum))
        else:
            return self.NodeInfo(minimum = min(left.minimum,right.minimum,root.val),maximum = max(root.val,left.maximum,right.maximum),valid = False)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isvalid(root).valid            
        # if root is None:
        #     return True
        # self.isValidBST(root.left)
        # self.isValidBST(root.right)
        # if root.val > self.minVal(root) and root.val < self.maxVal(root):
        #     return True
        # return False
  




