# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        l = root.left
        r = root.right
        root.left = None
        self.flatten(l)
        self.flatten(r)
        root.right = l
        curr_node = root
        while curr_node.right:
            curr_node = curr_node.right
        curr_node.right = r