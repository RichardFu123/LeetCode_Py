class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        all = 0
        n = len(s)
        start_end_paris = [(x,x) for x in range(n)] + [(x,x+1) for x in range(n-1)]
        for (b,e) in start_end_paris:
            while b>=0 and e<n and s[b]==s[e]:
                all+=1
                b-=1
                e+=1
        return all
