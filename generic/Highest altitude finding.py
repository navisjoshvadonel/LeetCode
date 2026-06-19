class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alti = 0
        curr_alti = 0

        for g in gain:
            curr_alti += g
            if curr_alti > max_alti:
                max_alti = curr_alti
        return max_alti