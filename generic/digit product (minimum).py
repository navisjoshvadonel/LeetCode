class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def help(num):
            product = 1
            while num>0:
                product *= num % 10
                num //= 10
            return product
        dummy = n 
        while True:
            if help(dummy) % t == 0:
                return dummy
            dummy+=1
