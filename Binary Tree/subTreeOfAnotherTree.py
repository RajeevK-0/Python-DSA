# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def trav(self,root,l):
        if root is None:
            l.append(None)
        else:
            l.append(root.val)
            self.trav(root.left,l)
            self.trav(root.right,l)
        return l
    def sameTree(self,root,subroot):
        if root is None and subroot is None:
            return True
        if root is None or subroot is None:
            return False
        if root and subroot and root.val == subroot.val:
            if self.sameTree(root.left,subroot.left) and self.sameTree(root.right,subroot.right):
                return True
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        if subRoot is None:
            return True    
        if root and subRoot and root.val == subRoot.val:
            if self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


        # l1 = self.trav(root,[])
        # l2 = self.trav(subRoot,[])
        # n1 = len(l1)
        # n2 = len(l2)
        # for i in range(n1):
        #     if l1[i] == l2[0]:
        #         for j in range(n2):
        #             if j == n2 and l2[j] == l1[i+j]:
        #                 return True
        #             if l2[j] == l1[i+j]:
        #                 continue
        #             else:
        #                 break
        # return False
        # print(l1)
        # print(l2)
        # if len(l1) == len(l2):
        #     if l1 == l2:
        #         return True
        #     return False
        # if len(l2) == 1:
        #     j = 0
        #     while l2[0] != l1[j]:
        #         if j == len(l1):
        #             return False
        #         j+=1 
        #     return True
        # i=0
        # while l2[0] != l1[i]:
        #     i+=1
        # newL = []
        # for j in range(len(l2)):
        #     newL.append(l1[i+j])
        # return newL == l2
        