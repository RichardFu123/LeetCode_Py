class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        vow=[]
        for i in range(len(s)):
            if s[i] not in 'aeiouAEIOU':
                res+=s[i]
            else:
                vow.append([i,s[i]])
                res+=' '
        res=list(res)
        for i in range(len(vow)):
            res[vow[i][0]]=vow[-i-1][1]
        return ''.join(res)
