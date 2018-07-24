class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        res=''
        l+=s.split(' ')
        for i in l:
            res+=(i[::-1]+' ')
        return res[:-1]
