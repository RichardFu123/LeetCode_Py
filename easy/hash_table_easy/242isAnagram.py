class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        a=list(s)
        b=list(t)
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False
