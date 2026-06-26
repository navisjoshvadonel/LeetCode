"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        result = []
        
        # Traverse the tree using a 'root-right-left' pattern
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push children left-to-right so the rightmost child 
            # is processed first (LIFO order)
            if node.children:
                for child in node.children:
                    stack.append(child)
        
        # Reverse the result to get the correct 'left-right-root' postorder
        return result[::-1]