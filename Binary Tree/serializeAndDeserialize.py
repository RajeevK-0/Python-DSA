# if Only unique values in Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def travPre(self,root,res):
        if root is None:
            return 
        res.append(str(root.val))
        self.travPre(root.left,res)
        self.travPre(root.right,res)
        return res
    def travInord(self,root,res):
        if root is None:
            return 
        self.travInord(root.left,res)
        res.append(str(root.val))
        self.travInord(root.right,res)
        return res
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        pre = self.travPre(root,[])
        inord = self.travInord(root,[])
        return ','.join(pre)+'#'+','.join(inord)
        # ans = ''
        # p = len(pre)
        # i = len(inord)
        # ans += str(p)
        # for j in range(p):
        #     ans += str(pre[j])
        # ans += str(i)
        # for j in range(i):
        #     ans += str(inord[j])
        # return ans
        # if root is None:
        #     return []
        # dq = deque()
        # dq.append(root)
        # res = []
        # while dq:
        #     t = dq.popleft()
        #     res.append(t.val)
        #     if t.left.val:
        #         dq.append(t.left)
        #     else :
        #         dq.append(None)
        #     if t.right.val:
        #         dq.append(t.right)
        #     else :
        #         dq.append(None)
    # Decodes your encoded data to tree.
    def trav(self,pre,ps,pe,inord,Is,Ie,d):
        if ps>pe or Is>Ie:
            return None
        start = int(pre[ps])
        mid = d[start]
        left = self.trav(pre,ps+1,ps+mid-Is,inord,Is,mid-1,d)
        right = self.trav(pre,ps+mid-Is+1,pe,inord,mid+1,Ie,d)
        root = TreeNode(left = left,right = right,val = start)
        return root
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        stpre , stinord = data.split('#')
        pre = stpre.split(',')
        inord = stinord.split(',')
        d = {}
        for i in range(len(inord)):
            d[int(inord[i])] = i
        return self.trav(pre,0,len(pre)-1,inord,0,len(inord)-1,d)
        