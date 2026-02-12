# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def inOrd(self,root,k,res):
    #     if root is None:
    #         return root
    #     self.inOrd(root.left,k,res)
    #     res.append(root.val)
    #     self.inOrd(root.right,k,res)
    class nodeinfo:
        def __init__(self,count = 0 , kelement = 0):
            self.count = count
            self.kelement = kelement
    def trav(self,root):
        pass
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        # res =[]
        # self.inOrd(root,k,res)
        # return res[k-1]