# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def bst(self,root,mn,mx):
    #     if root is None:
    #         return True
    #     self.bst(root.left,min(root.val,mn),max(root.val,mx))
    #     self.bst(root.right,min(root.val,mn),max(root.val,mx))
    #     if root.val >= mn and root.val < mx:
    #         return True
    #     else:
    #         return False
    # def minVal(self,root):
    #     mn = 1001
    #     if root is None:
    #         return 0
    #     curr = root
    #     while curr:
    #         mn = min(curr.val,mn)
    #         curr = curr.left
    #     return mn
    # def maxVal(self,root):
    #     mx = -1001
    #     if root is None:
    #         return 0
    #     curr = root
    #     while curr:
    #         mx = max(curr.val,mx)
    #         curr = curr.right
    #     return mx
    # def leftTree(self,root,mn,mx):
    #     if root is None:
    #         return 0
    #     self.leftTree(root.left,mn,mx)
    #     self.leftTree(root.right,mn,mx)
    #     return mn = min(root.val,mn)
    #     return mx = max(root.val,mx)
    #     if root.val > 
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
  




