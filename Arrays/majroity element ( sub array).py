class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        count_valid = 0
        for i in range(n):
            target_freq = 0
            for j in range(i,n):
                if nums[j] == target:
                    target_freq +=1
                length = j - i + 1
                if 2*target_freq>length:
                    count_valid +=1
        return count_valid