class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = 0
        for _ in num:
            n+=1

        ans = 0.0
        def expec(c):
            return 4.5 if c =='?' else int(c)

        for i in range(n //2):
            ans+=expec(num[i])
        for i in range(n//2 ,n):
            ans-=expec(num[i])
        return ans!= 0.0

        