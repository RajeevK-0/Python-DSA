# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def trav(self,preorder,ps,pe,inorder,Is,Ie,d):
        if ps > pe or Is > Ie:
            return None
        start = preorder[ps]
        mid = d[start]
        root = TreeNode(val = start)
        left = self.trav(preorder,ps+1,ps+mid-Is,inorder,Is,mid-1,d)
        right = self.trav(preorder,ps+mid-Is+1,pe,inorder,mid+1,Ie,d)
        root = TreeNode(left = left,right = right)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i
        return self.trav(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,d)