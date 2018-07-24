class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        t = x ^ y
        count = 0
        while t != 0:
            count = count + 1
            t = t & (t-1)
        return count
