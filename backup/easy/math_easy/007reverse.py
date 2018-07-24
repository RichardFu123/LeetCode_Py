class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10 :
            return x
        n1=abs(x) 
        b=str(n1)
        if len(b)>10:
            return 0
        v=''
        for i in range(len(b)):
            v=v+b[-(i+1)]
        result=int(v)    
        if x<0: 
            result=-result
        if -2147483648 < result < 2147483647:
            return result
        else:
            return 0
