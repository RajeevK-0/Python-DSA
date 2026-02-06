# def findMin(tree):
#     return MinNode(tree.root)
# def MinNode(root):
#     if root is not None:
#         MinNode(root.left)
#         if root.left == None:
#             return root.item
def findMin(tree,temp):
    curr = temp
    while curr.left is not None:
        curr = curr.left
    return curr.item

# def findMax(tree):
#     return MaxNode(tree.root)
# def MaxNode(root):
#     if root is not None:
#         MaxNode(root.right)
#         if root.right == None:
#             return root.item

def findMax(tree,temp):
    curr = temp 
    while curr.right is not None:
        curr = curr.right
    return curr.item

# def deleteNode(tree,val):
#     if val > findMax(tree.root) or val< findMin(tree.root):
#         raise ValueError("No Node of that val in tree")
#     else:
#         pass
def delete(tree,data):
    tree.root = tree.rdelete(tree.root,data)
def rdelete(tree,root,data):
    if root is None:
        return root
    if data <root.item:
        root.left = tree.rdelete(root.left,data)
    elif data > root.item:
        root.right = tree.rdelete(root.right,data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.item = tree.findMin(root.right)
        tree.rdelete(root.right,root.item)
    return root
def size(tree):
    return len(tree.inorder())  