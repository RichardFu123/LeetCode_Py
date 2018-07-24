class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        m=0
        n=0
        c=collections.Counter(s)
        for i in c:
            if c[i]%2==0:
                l+=c[i]
        for j in c:
            if c[j]%2==1:
                m=max(m,1)
                n+=int(c[j]-1)
        
        return l+n+m
