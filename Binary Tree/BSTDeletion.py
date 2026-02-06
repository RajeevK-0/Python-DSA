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
def deleteNode(tree,val):
    if val > findMax(tree.root) or val< findMin(tree.root):
        raise ValueError("No Node of that val in tree")
    else:
        pass