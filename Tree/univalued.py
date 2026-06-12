# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        target = root.val
        def check(node):
            if not node:
                return True
            if node.val != target:
                return False

            return check(node.left) and check(node.right)
        return check(root)