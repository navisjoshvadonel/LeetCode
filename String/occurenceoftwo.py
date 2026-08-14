class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        l = 0
        max_len = 0
        for right in range(len(s)):
            idx = ord(s[right])-ord('a')
            freq[idx] +=1
            while freq[idx] >2:
                freq[ord(s[l]) - ord('a')] -=1
                l +=1
            max_len = max(max_len,right-l+1)
        return max_len
        

        