# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        if curr is None:
            return []
        res = []
        dq = deque()
        dq.append(root)
        while dq:
            sz = len(dq) 
            for i in range(sz):
                t = dq.popleft()
                if t.left:
                    dq.append(t.left)
                if t.right:
                    dq.append(t.right)
                if i == sz-1:
                    res.append(t.val)
        return res