# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Recursive solution
        # if q.val > p.val:
        #     if p.val <= root.val <= q.val:
        #         return root
        # else:
        #     if q.val <= root.val <= p.val:
        #         return root
        # if root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        # Iterative solution
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root:
            if root.val > large: 
                root = root.left
            elif root.val < small: 
                root = root.right
            else: 
                return root
        return None