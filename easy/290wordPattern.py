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


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a=str.split(' ')
        b=pattern
        if len(b)!=len(a):
            return False
        c=[]
        dic={}
        for i in range(len(b)):
            if b[i] in dic:
                c.append(dic[b[i]])
            else:
                dic[b[i]]=a[i]
                c.append(dic[b[i]])
        if len(set(dic.values()))!=len(set(b)):
            return False
        return a==c


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a=str.split(' ')
        b=pattern
        if len(b)!=len(a):
            return False
        dic={}
        for i in range(len(b)):
            if b[i] in dic:
                if dic[b[i]]!=a[i]:
                    return False
            else:
                dic[b[i]]=a[i]
        if len(set(dic.values()))!=len(set(b)):
            return False
        return True


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a=str.split(' ')
        z=zip(a,pattern)
        return (len(set(a))==len(set(pattern))==len(set(z)) and len(a)==len(pattern))

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return (len(set(str.split()))==len(set(pattern))==len(set(zip(str.split(),pattern))) and len(str.split())==len(pattern))
