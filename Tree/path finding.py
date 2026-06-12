# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """  
        paths = []
        def depth(node, curr_path):
            if not node:
                return
            if not curr_path:
                curr_path = str(node.val)    
            else:
                curr_path += "->"+str(node.val)

            if not node.left and not node.right:
                paths.append(curr_path)
                return
            depth(node.left,curr_path)
            depth(node.right,curr_path)        
        depth(root,"")
        return paths