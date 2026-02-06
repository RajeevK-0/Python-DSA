def traversalBT(tree):
    res = []
    return rtraverse(tree.root,res)
def rtraverse(root,result):
    if root:
        result.append(root.item)
        rtraverse(root.left,result)
        rtraverse(root.right,result)