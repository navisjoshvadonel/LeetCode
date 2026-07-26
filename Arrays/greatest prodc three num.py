class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        min1 = min2 = float('inf')
        max1=max2=max3=float('-inf')

        for n in nums:
            if n < min1:
                min2 = min1
                min1 = n
            elif n <min2:
                min2 = n
            if n > max1:
                max3=max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3=max2
                max2 = n
            elif n >max3:
                max3 = n
        product1 = min1 * min2 * max1
        product2 = max1 * max2 * max3

        if product1 > product2:
            return product1
        else:
            return product2

        