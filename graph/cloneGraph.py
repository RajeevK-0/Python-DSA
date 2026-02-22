"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def dfs(self,node,d):     
        if node in d:
            return node
        NewNode = Node()
        NewNode.val = node.val
        d[node] = NewNode
        for i in range(len(node.neighbors)):
            NewNode.neighbors.append(self.dfs(node.neighbors[i],d))
        return NewNode
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        d = {}
        return self.dfs(node,d)