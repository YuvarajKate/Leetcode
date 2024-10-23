# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # If we find the node with the target value, return it
        if root.val == val:
            return root
        
        # If the target value is smaller than the current node's value, search in the left subtree
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        # If the target value is larger, search in the right subtree
        else:
            return self.searchBST(root.right, val)