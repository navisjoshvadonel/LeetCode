class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :type rtype: bool
        """
        return (len(s) == len(goal)) and (goal in (s + s))