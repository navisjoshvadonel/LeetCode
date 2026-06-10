class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
            if nums[i] == target:
                count +=1
            else:
                count -=1
        return target