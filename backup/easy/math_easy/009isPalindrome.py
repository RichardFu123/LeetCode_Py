class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if 0<x<10:
            return True
        s= str(x)
        for i in range(len(s)):
            if s[i]!=s[-i-1]:
                return False
        return True
