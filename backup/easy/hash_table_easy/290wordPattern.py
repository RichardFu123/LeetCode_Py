class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a=[]
        b=[]
        c=[]
        a=str.split(' ')
        b=list(pattern)
        c=zip(a,b)
        if len(set(a))==len(set(b))==len(set(c)) and len(a)==len(b):
            return True
        else:
            return False
