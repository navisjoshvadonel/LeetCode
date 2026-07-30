class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        length = len(word)
        pushes = 0
        for i in range(length):
            pushes += (i//8) + 1
        return pushes
        