# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recBuild(stop):
            # inorder[-1] is the value related to last node of the last level of the tree
            if postorder and inorder[-1] != stop:
                # keep popping from postorder until we reach inorder[-1]
                root = TreeNode(postorder.pop())
                # all the popped nodes are root nodes of a postorder traversal
                root.right = recBuild(root.val)
                
                # popping from inorder since we have already seen this node
                inorder.pop()
                # build the left side
                root.left = recBuild(stop)
                return root
        return recBuild(None)