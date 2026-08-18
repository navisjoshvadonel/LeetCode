class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 1:
            max_val = -1
            for i in range(n):
                count = 0
                for j in range(n):
                    if nums[j] == nums[i]:
                        count += 1
                if count == 1:
                    if nums[i] > max_val:
                        max_val = nums[i]
            return max_val
            
        elif k == n:
            max_val = nums[0]
            for i in range(1, n):
                if nums[i] > max_val:
                    max_val = nums[i]
            return max_val
            
        else:
            candidates = []
            if nums[0] not in candidates:
                candidates.append(nums[0])
            if nums[n-1] not in candidates:
                candidates.append(nums[n-1])
                
            ans = -1
            for candidate in candidates:
                subarrays_count = 0
                for i in range(n - k + 1):
                    found = False
                    for j in range(i, i + k):
                        if nums[j] == candidate:
                            found = True
                            break
                    if found:
                        subarrays_count += 1
                
                if subarrays_count == 1:
                    if candidate > ans:
                        ans = candidate
                        
            return ans