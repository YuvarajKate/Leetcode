"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # A mapping from original nodes to cloned nodes
        cloned_nodes: Dict[Node, Node] = {}

        def dfs(current_node: Node) -> Node:
            if current_node in cloned_nodes:
                return cloned_nodes[current_node]
            
            # Clone the current node
            clone = Node(current_node.val)
            cloned_nodes[current_node] = clone
            
            # Recursively clone all neighbors
            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)