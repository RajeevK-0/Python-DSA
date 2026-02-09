# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root,1]]
        res = 0
        while stack :
            n,dpth = stack.pop()
            if n:
                res = max(res,dpth)
                stack.append([n.left,dpth+1])
                stack.append([n.right,dpth+1])
        return res
        
        # return 1+ max(self.maxDepth(root.right),self.maxDepth(root.left))
        
        # q = deque([root])
        # lvl = 0
        # while q:
        #     for i in range(len(q)):
        #         n = q.popleft()
        #         if n.left:
        #             q.append(n.left)
        #         if n.right:
        #             q.append(n.right)
        #     lvl +=1
        # return lvl