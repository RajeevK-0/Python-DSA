# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lvlOrd(self,root,result):
        dq = deque()
        if root is None:
            return []
        dq.append(root)
        while dq :
            r = []
            sz = len(dq)
            for i in range(sz):
                t = dq.popleft()
                r.append(t.val)
                if t.left is not None:
                    dq.append(t.left)
                if t.right is not None:
                    dq.append(t.right)
            result.append(r)        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.lvlOrd(root,res)
        return res