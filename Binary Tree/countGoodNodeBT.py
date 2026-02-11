# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def preTrav(self,root,result,count):
    #     if root is not None:
    #         result.append(root.val)
    #         if root.left is None and root.right is None:
    #             result.append(None)
    #         self.preTrav(root.left,result,count)
    #         if root.left is not None:
    #             if root.left.val > root.val:
    #                 count += 1
    #         self.preTrav(root.right,result,count)
    #         if root.right is not None:
    #             if root.right.val > root.val:
    #                 count += 1
    def postCount(self,root,mx):
        if root is None:
            return 0
        leftcount = self.postCount(root.left,max(mx,root.val))
        rightcount = self.postCount(root.right,max(mx,root.val))
        if root.val >= mx:
            return 1+leftcount+rightcount
        else:
            return leftcount+rightcount
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        mx = -101
        return self.postCount(root,mx)
        # res = []
        # count = 1
        # if root is not None:
        #     self.preTrav(root,res,count)
        # return count
        # good = 0
        # m = 0
        # if root is not None:
        #     self.preTrav(root,res)
        #     print(res)
        #     for i in range(1,len(res)):
        #         t = m
        #         if res[i] is not None:    
        #             m = max(m,res[i])
        #         if m != t:
        #             good+=1
        #         if res[i] == None:
        #             good+=1
        # return good