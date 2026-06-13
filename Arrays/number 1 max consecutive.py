class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        initial = 0
        final = 0 
        for n in nums:
            if n == 1:
                initial +=1
            else:
                if initial>final:
                    final = initial
                initial = 0 
        return max(initial,final)