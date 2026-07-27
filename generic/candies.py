class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        total_candies = 0
        for _ in candyType:
            total_candies += 1
            
        max_allowed = total_candies // 2
        seen_types = {}
        unique_types = 0
        for candy in candyType:
            if candy not in seen_types:
                seen_types[candy] = True
                unique_types += 1
                
        if unique_types < max_allowed:
            return unique_types
        else:
            return max_allowed
