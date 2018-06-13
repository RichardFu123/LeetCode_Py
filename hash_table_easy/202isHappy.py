class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = set()
        while not n in c:
            c.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n==1
        #return 1 in c
