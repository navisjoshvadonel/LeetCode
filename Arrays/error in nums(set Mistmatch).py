class Solution(object):
    def findErrorNums(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]