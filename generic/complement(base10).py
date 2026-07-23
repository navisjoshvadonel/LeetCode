class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        binary = 1
        while binary <=n:
            binary <<=1
        binary -=1
        return n ^ binary
