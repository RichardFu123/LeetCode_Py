class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c=collections.Counter(moves)
        lr=True
        ud=True
        try:
            if c['L']!=c['R']:
                lr=False
        except:
            pass
        try:
            if c['U']!=c['D']:
                ud=False
        except:
            pass
        return lr and ud

        
