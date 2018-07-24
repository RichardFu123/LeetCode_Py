class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a=list(s)
        b=list(t)
        for i in a:
            b.remove(i)
        return str().join(b)
