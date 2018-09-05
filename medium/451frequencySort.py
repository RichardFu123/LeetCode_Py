class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=sorted(list(s))
        cut=[]
        forw=0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                cut.append(''.join(s[forw:i+1]))
                forw=i+1
        cut.append(''.join(s[forw:]))
        cut.sort(key=lambda X:len(X))
        cut.reverse()
        return ''.join(cut)
