class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <3:
            return -1
        a,b,c = nums[0],nums[1] , nums[2]

        if (a>b and a<c) or (a>c and a<b):
            return a
        if (b>a and b<c) or (b>c and b<a):
            return b
        return c