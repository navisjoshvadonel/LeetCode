class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        left , right = 0 , num //2
        
        while left <= right:
            mid = (left + right) //2
            guess = mid * mid

            if guess == num:
                return True
            if guess <num:
                left = mid + 1
            else:
                right = mid - 1
        return False