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
    
    # class nodeinfo:
    #     def __init__(self,count = 0 , kelement = None):
    #         self.count = count
    #         self.kelement = kelement
    
    # def trav(self,root,k):
    #     if root is None:
    #         return self.nodeinfo()
    #     left = self.trav(root.left,k)
    #     if left.kelement is not None:
    #         return left
    #     if left.count+1 == k:
    #         return self.nodeinfo(left.count+1,root.val)
    #     right = self.trav(root.right,k-(left.count+1))
    #     if right.kelement is not None:
    #         return right
    #     return self.nodeinfo(left.count+1+right.count,None)
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