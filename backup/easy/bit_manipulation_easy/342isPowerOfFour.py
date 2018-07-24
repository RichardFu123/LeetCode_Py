class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        s='{:b}'.format(num)
        if s.count('1')==1:
            if len(s)%2==1:
                return True
        return False
