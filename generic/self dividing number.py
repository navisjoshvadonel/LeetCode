class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left , right+1):
            if self.isSelfDividing(num):
                result.append(num)
        return result

    def isSelfDividing(self,n):
        t = n
        while t>0:
            digit = t % 10
            if digit == 0 or n % digit != 0:
                return False
            t //=10
        return True