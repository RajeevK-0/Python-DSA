from collections import deque
class Node:
    def __init__(self,val = None,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None

    def insert(self, item):
        self.root = self.rinsert(self.root,item)
    
    def rinsert(self,root,item):
        if root is None:
            root = Node(val=item)
        elif root.val < item:
            root.right = self.rinsert(root.right,item)
        elif root.val > item:
            root.left = self.rinsert(root.left,item)
            # if root.val > item:
            #     root.right = Node(val=item)
            # elif root.val <item:
            #     root.left = Node(val=item)
        return root
    
    def inorder(self):
        res = []
        self.rinorder(self.root,res)
        return res
    
    def rinorder(self,root,res):
        if root is not None:
            self.rinorder(root.left,res)
            res.append(root.val)
            self.rinorder(root.right,res)
    
    def preorder(self):
        res = []
        self.rpreorder(self.root,res)
        return res
    
    def rpreorder(self,root,res):
        if root is not None:
            res.append(root.val)
            self.rpreorder(root.left,res)
            self.rpreorder(root.right,res) 
    
    def postorder(self):
        res = []
        self.rpostorder(self.root,res)
        return res
    
    def rpostorder(self,root,res):
        if root is not None:
            self.rpostorder(root.left,res)
            self.rpostorder(root.right,res)
            res.append(root.val)

    def MinVal(self,root):
        t = root
        while t.left is not None:
            t = t.left
        return t
    
    def MaxVal(self,root):
        t = root
        while t.right is not None:
            t = t.right
        return t
    
    def search(self,item):
        return self.rsearch(self.root,item)
    
    def rsearch(self,root,item):
        if root.val == item or root is None:
            return root
        elif root.val > item:
            return self.rsearch(root.left,item)
        else:
            return self.rsearch(root.right,item)
    
    def deletion(self,item):
        self.root = self.rdelete(self.root,item)
        # t = self.search(item)
        # if t.right == None and t.left == None:
        #     t.val = None
        # elif t.left is None:
        #     t.val = t.right.val
        # elif t.right is None:
        #     t.val = t.left.val
        # else:
        #     minValue = self.MinVal(t.right)
        #     t.val = minValue.val
        #     self.deletion(t.right,minValue)
    def rdelete(self,root,item):
        if root is None :
            return None
        elif root.val > item:
            root.left = self.rdelete(root.left,item)
        elif root.val < item:
            root.right = self.rdelete(root.right,item)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            t = self.MinVal(root.right)
            root.val = t.val
            root.right = self.rdelete(root.right,t.val)
        return root
    def BFS(self):
        if self.root is None:
            return []
        res = []
        q = deque([self.root])
        while q:
            for i in range(len(q)):
                n = q.popleft()
                res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return res
if __name__ == "__main__":
    tr = BST()
    tr.insert(100)
    tr.insert(90)
    tr.insert(80)
    tr.insert(160)
    tr.insert(190)
    tr.insert(170)
    print(tr.inorder())
    print(tr.postorder())
    print(tr.preorder())
    print(tr.search(190).left.val)
    print("*"*20)
    tr.deletion(170)
    print(tr.inorder())
    print(tr.BFS())
