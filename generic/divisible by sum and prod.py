class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = n
        sum1 = 0
        prod = 1
        while t>0:
            digit =  t % 10
            sum1 +=digit
            prod *=digit
            t //= 10
        total = sum1 + prod
        return n %total == 0 if total !=0 else False
