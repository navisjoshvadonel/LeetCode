class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_val = nums[0]
        for num in nums:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num
        a,b = min_val , max_val
        while a:
            a,b = b%a , a
        return b