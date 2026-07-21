class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num += 2 **32
        hex = "0123456789abcdef"
        result =[]

        while num >0:
            rem = num % 16
            result.append(hex[rem])
            num //= 16
        return "".join(result[::-1])
        