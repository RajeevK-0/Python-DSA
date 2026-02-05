class Node:
    def __init__(self,item = None,left= None,right= None):
        self.item = item
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def insert(self,item):
        self.root = self.rinsert(self.root,item)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.left = self.rinsert(root.left,data)
        elif data>root.item:
            root.right = self.rinsert(root.right , data)
        return root
    def search(self,item):
        return self.rsearch(self.root,item)
    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    def inorder(self):
        res = []
        self.rinorder(self.root,res)
        return res
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        res = []
        self.rpreorder(self.root,res)
        return res
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    def postorder(self):
        res = []
        self.rpostorder(self.root,res)
        return res
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)