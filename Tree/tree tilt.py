# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total = 0
        def get_sum(node):
            if not node:
                return 0
            left_sum = get_sum(node.left)
            right_sum = get_sum(node.right)
            self.total += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        get_sum(root)
        return self.total