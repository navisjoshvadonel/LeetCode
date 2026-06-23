class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        x_net = moves.count('R')- moves.count('L')
        y_net = moves.count('U')- moves.count('D')

        wild = moves.count('_')

        return abs(x_net)+abs(y_net)+wild