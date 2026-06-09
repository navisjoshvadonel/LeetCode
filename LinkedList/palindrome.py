# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        empty = []
        current = head
        if current == None:
            return False
        while current:
            empty.append(current.val)
            current = current.next
        return empty == empty[::-1]