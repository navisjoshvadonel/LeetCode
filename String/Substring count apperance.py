class Solution(object):
    def numberOfSubstrings(self, s):
        last_a = last_b = last_c = -1
        res = 0
        
        for i in range(len(s)):
            if s[i] == 'a':
                last_a = i
            elif s[i] == 'b':
                last_b = i
            else:
                last_c = i
            
            res += min(last_a, last_b, last_c) + 1
        
        return res