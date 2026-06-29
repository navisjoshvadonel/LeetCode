class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x <0 else 1
        x = abs(x)

        reverse = int(str(x)[::-1]) * sign
        if reverse < -2**31 or reverse> 2**31:
            return 0
        return reverse