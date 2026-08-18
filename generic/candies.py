class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        #candies calculation manually 
        total_candies = 0
        for _ in candyType:
            total_candies += 1
        #GIVEN THAT THE SISTER CAN ONLY HAVE HALF OF THE CANDIES     
        max_allowed = total_candies // 2
        #UNIQUE TYPES OF CANDIES
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
