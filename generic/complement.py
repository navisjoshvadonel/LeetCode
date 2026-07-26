class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        binary = 0
        while temp > 0:
            binary = (binary <<1) | 1
            temp >>=1
        return binary ^ num
        
        